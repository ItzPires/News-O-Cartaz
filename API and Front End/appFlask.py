from flask import Flask, render_template, request as requestF
import psycopg2, random, re, json, urllib, datetime
from requests_html import HTMLSession

app = Flask(__name__)

citys = []
htmlWeather = set()

class City:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class HtmlWeather:
  def __init__(self, html, id):
    self.html = html
    self.id = id

def createLink(url, sleep):
    s = HTMLSession()
    r = s.get(url)

    if(sleep == True):
        r.html.render(sleep = 1)

    return r

def readCitys():
    file = open("city.weather", "r", encoding='utf-8')
    file2 = open("html.weather", "r", encoding='utf-8')
    
    for i in file:
        l = i.split(";")
        city = City(l[1].strip("\n"), l[0].strip(" "))
        citys.append(city)

    for i in file2:
        l = i.split(";")
        html = HtmlWeather(l[1].strip("\n"), int(l[0]))
        htmlWeather.add(html)

    file.close()
    file2.close()

readCitys()

def getCovidApi(url):
    r = createLink(url, False)
    
    jsonObj = r.html.text
    todayCases = int(jsonObj.split('"todayCases":')[1].split(',"deaths"')[0])
    todayRecovered = int(jsonObj.split('"todayRecovered":')[1].split(',"active"')[0])
    todayDeaths = int(jsonObj.split('"todayDeaths":')[1].split(',"recovered"')[0])

    return ["COVID", todayCases, todayRecovered, todayDeaths]

def covidAPI():
    url = "https://disease.sh/v3/covid-19/countries/pt"
    url2 = "https://disease.sh/v3/covid-19/countries/pt?yesterday=true"

    dayNow = datetime.datetime.now()
    l = getCovidApi(url)

    if(int(dayNow.strftime("%H")) <= 11):
        dayNow = dayNow - datetime.timedelta(days=1)

    if(l[1] == 0 and l[2] == 0 and l[3] == 0):
        l = getCovidApi(url2)
        dayNow = dayNow - datetime.timedelta(days=1)

    dayStr = dayNow.strftime("%d/%m/%Y")

    l.append(dayStr)

    return l

def weatherAPI(day, city):
    url= "http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/hp-daily-forecast-day" + str(day) +".json"

    myCity = ""

    if (city == ""):
        try:
            ip = requestF.remote_addr

            urlIP = "https://ipinfo.io/" + ip + "/json"

            resposta = urllib.request.urlopen(urlIP).read()
            JSON_object = json.loads(resposta.decode('utf-8'))

            myCity = JSON_object['region']
        except:
            myCity = "Lisboa"
    else:
        myCity = city

    myCityObj = None

    for i in citys:
        if(i.name == myCity):
            myCityObj = i
            break
    
    if(myCityObj == None):
        myCityObj = City("Lisboa", 1110600)

    resposta = urllib.request.urlopen(url).read()
    JSON_object = json.loads(resposta.decode('utf-8'))

    dayAux = JSON_object['forecastDate'].split("-")
    day = datetime.datetime(int(dayAux[0]), int(dayAux[1]), int(dayAux[2]))
    
    dayName = day.weekday()
    
    data = JSON_object['data']

    tempoMax = 0
    tempoMin = 0
    typeWeatherHtml = 0
    
    for i in data:
        if(i['globalIdLocal'] == int(myCityObj.id)):
            tempoMax = i['tMax']
            tempoMin = i['tMin']
            typeWeather = i['idWeatherType']

    for i in htmlWeather:
        if (i.id == typeWeather):
            typeWeatherHtml = i.html
    
    return [myCity , tempoMax, tempoMin, dayName, typeWeatherHtml]

def gamesResult():
    r = createLink("https://maisfutebol.iol.pt/resultadoseclassificacoes/2021-08-28", False)

    classe = '//*[@class="JgTerminado"]'
    clubes = ["FC Porto", "2sDzOhWg-QZCjjEXi.png", "Sporting", "OWbPc9il-WYr1gV4A.png", "Estoril", "pEIK5GfM-hz6r3c7O.png", "Benfica", "", "Boavista", "Portimonense", "Braga", "Gil Vicente", "V. Guimarães", "Marítimo", "Vizela", "Tondela", "Paços Ferreira", "Arouca", "Moreirense", "Famalicão", "WIxnhCGG-feEUYmCc.png", "Belenenses", "	Santa Clara", ""]

    information = r.html.xpath(classe)

    final = ["GAMES"]

    for i in information:
        try:
            gameHouse = i.html.split('class="team1Cell">')[1].split('</span></a>')[0]
            gameVisitor = i.html.split('class="team2Cell">')[1].split('</span></a>')[0]
            resultHouse = i.html.split('<span class="middleCell resultCell">')[1].split('</span>')[0]
            resultVisitor = i.html.split('<span class="middleCell resultCell">')[2].split('</span>')[0]
            if(gameHouse in clubes and gameVisitor in clubes):
                url1 = url2 = ""
                for j in range(len(clubes)):
                    if(clubes[j] == gameHouse):
                        url1 = url1 + clubes[j]
                    if(clubes[j] == gameVisitor):
                        url2 = url2 + clubes[j]
                aux = [url1, resultHouse, resultVisitor, url2]
                final.append(aux)
        except:
            pass
        #break
    return final

def gerarAnuncios(news, numAds):
    anuncio = [["TREE","Quer anunciar aqui? Entre em Contacto","Email"],["ADD","Quer anunciar aqui? Entre em Contacto","Email"],["ADD","Quer as notícias do seu site aqui? Entre em Contacto","Email"]]

    pos = 6

    size = len(news) - pos
    final = news

    if(numAds == 0):
        numAds = size//10

    if(numAds == 0):
        numAds = 1

    passo = size//numAds

    for i in range(numAds):
        anuncioPos = random.randint(0,2)
        final.insert(pos,anuncio[anuncioPos])
        pos = pos + passo

    weather = weatherAPI(0, "")
    weather.insert(0,"TEMPO")
    auxPos = random.randint(2, 6)
    final.insert(auxPos, weather)

    covid = covidAPI()
    auxPos = random.randint(4, 7)
    final.insert(auxPos, covid)

    #games = gamesResult()
    #auxPos = random.randint(3, 7)
    #final.insert(auxPos, games)

    return final

def executeInDB(command):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(command)
    news = cur.fetchall()
    conn.close()

    return news

def getLocais():
    command = ""
    searchRequest = requestF.args.get('search')

    if(searchRequest == None):
        command = "SELECT * FROM news where categoria = 'Norte' order by data desc limit 3"
        newsN = executeInDB(command)
        command = "SELECT * FROM news where categoria = 'Centro' order by data desc limit 3"
        newsC = executeInDB(command)
        command = "SELECT * FROM news where categoria = 'Sul' order by data desc limit 3"
        newsS = executeInDB(command)
    else:
        searchRequest = re.sub(r'[^\w]', '', searchRequest)
        command = "SELECT * FROM news where upper(titulo) like upper('%"+ searchRequest +"%') order by data desc"
        newsN = executeInDB(command)
        newsC = executeInDB(command)
        #redirecionar depois
    return newsN, newsC, newsS

def base(limit, where, numAds):
    command = ""
    seeAll = True
    searchRequest = requestF.args.get('search')

    if(searchRequest == None):
        if(limit == True):
            command = "SELECT * FROM news " + where + " order by data desc limit 14"
        else:
            command = "SELECT * FROM news " + where + " order by data desc"
        seeAll = False
    else:
        searchRequest = re.sub(r'[^\w]', '', searchRequest)
        command = "SELECT * FROM news where upper(titulo) like upper('%"+ searchRequest +"%') order by data desc"
        seeAll = True
    if(command == ""):
        print("Erro")
        return
    else:
        news = executeInDB(command)
        newsT = news.copy()
        news = gerarAnuncios(news, numAds)

    return newsT, news, seeAll

@app.route("/", methods = ["GET", "POST"])
def index():
    newsT, news, seeAll = base(limit = True, where = "where destaques = True", numAds = 2)

    return render_template('index.html', newsT = newsT, news = news, seeAll = seeAll)

@app.route("/all/destaques", methods = ["GET", "POST"])
def seeAllDestaques():
    newsT, news, seeAll = base(limit = False, where = "where destaques = True", numAds = 0)
    seeAll = True
    return render_template('index.html',newsT = newsT, news = news, seeAll = seeAll)

@app.route("/ultimas", methods = ["GET", "POST"])
def last():
    newsT, news, seeAll = base(limit = True, where = "where ultimas = True", numAds = 2)

    return render_template('last.html',newsT = newsT, news = news, seeAll = seeAll)

@app.route("/all/ultimas", methods = ["GET", "POST"])
def seeAllLast():
    newsT, news, seeAll = base(limit = False, where = "", numAds = 0)
    seeAll = True

    return render_template('last.html',newsT = newsT, news = news, seeAll = seeAll)

@app.route("/source/<keyword>", methods = ["GET", "POST"])
def allOfOne(keyword):
    keyword = re.sub(r'[^\D]', '', keyword)

    command = "SELECT * FROM news where upper(site) like upper('%"+ keyword +"%') order by data desc"

    news = executeInDB(command)

    if(len(news) == 0 or keyword == "" or keyword == None):
        return render_template('error.html', error = 404)

    newsT = news.copy()
    news = gerarAnuncios(news, 0)

    return render_template('index.html', keyword = keyword ,newsT = newsT, news = news)

@app.route("/tempo")
def weather():
    daysOfWeak = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo",]
    tempInfo = []

    cityG = requestF.args.get('cidade')
    cityS = ""

    if(cityG == None):
        pass
    else:
        cityS = cityG
    
    aux = weatherAPI(0, cityS)
    city = aux[0]
    aux.append("Hoje")
    tempInfo.append(aux)

    aux = weatherAPI(1, cityS)
    aux.append("Amanhã")
    tempInfo.append(aux)

    aux = weatherAPI(2, cityS)
    aux.append(daysOfWeak[aux[3]])
    tempInfo.append(aux)

    citysMy = citys.copy()

    for i in citys:
        if(city == i.name):
            citysMy.remove(i)

    auxCity = City(city, 000)
    citysMy.insert(0, auxCity)

    return render_template('weather.html', citys = citysMy, Temp = tempInfo, city = city)

def db_connection():
    connection = psycopg2.connect(user = "postgres",
        password = "postgres",   # password should not be visible - will address this later on the course
        host = "localhost",
        port = "5432",
        database = "dbfichas")
    # parameters should be changable - will adress this later on the course

    return connection

@app.route("/contacto")
def contacto():
    return render_template('contact.html')

@app.route("/fontes")
def fontes():
    return render_template('fontes.html')

@app.route("//help word")
def carbono():
    return render_template('carbono.html')

@app.route("/locais")
def locais():
    newsN, newsC, newsS = getLocais()
    seeMore = ("", "/", "https://static.thenounproject.com/png/943464-200.png", "Ver Mais")
    #newsN.append(seeMore)
    #newsC.append(seeMore)

    return render_template('locais.html', newsN = newsN, newsC = newsC, newsS = newsS)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/categoria/<keyword>", methods = ["GET", "POST"])
def categoria(keyword):
    keyword = re.sub(r'[^\w]', '', keyword)

    command = "SELECT * FROM news where upper(categoria) like upper('%" + keyword + "%') order by data desc"

    news = executeInDB(command)

    if(len(news) == 0 or keyword == "" or keyword == None):
        return render_template('error.html', error = 404)

    newsT = news.copy()
    news = gerarAnuncios(news, 0)

    return render_template('index.html', keyword = keyword ,newsT = newsT, news = news)

@app.route("/faq")
def brevemente():
  return render_template('brevemente.html', tag = "FAQ")

def page_not_found(e):
  return render_template('error.html', error = 404)

app.register_error_handler(404, page_not_found)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
