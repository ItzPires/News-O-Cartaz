from requests_html import HTMLSession
import psycopg2
import datetime
import time

categorias = ["Covid-19", "País",  "Economia", "Cultura", "Desporto", "Mundo"]

def getInformation(information, pos, https, split1, split2):
    try:
        url = https + information[pos].html.split(split1)[1].split(split2)[0]
        #print(url)
    except:
        url = ""
    
    return url

def db_connection():
    connection = psycopg2.connect(user = "postgres",
        password = "postgres",   # password should not be visible - will address this later on the course
        host = "localhost",
        port = "5432",
        database = "dbfichas")
    # parameters should be changable - will adress this later on the course

    return connection

def createLink(url, sleep):
    s = HTMLSession()
    r = s.get(url)

    if(sleep == True):
        r.html.render(sleep = 1)

    return r

def addDB(site, urlNews, urlImage, title, description, data, categoria, destaques, ultimas):
    try:
        conn = db_connection()
        cur = conn.cursor()
        statement = """
                    INSERT INTO news (site, url, url_imagem, titulo, descricao, data, categoria, destaques, ultimas) 
                            VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (site, urlNews, urlImage, title, description, data, categoria, destaques, ultimas)
        cur.execute(statement, values)
        cur.execute("commit")
    except (Exception, psycopg2.errors.UniqueViolation) as error:
        conn.close()
        statement = "Select * from news where url = '" + urlNews + "'"
        conn = db_connection()
        cur = conn.cursor()
        cur.execute(statement)
        obj = cur.fetchall()
        conn.close()

        if(obj[0][7] == destaques and obj[0][8] == ultimas):
            pass
        elif(obj[0][7] != destaques and obj[0][8] == ultimas):
            print("update destaques")
            statement = " UPDATE news SET destaques = " + destaques + "WHERE url = '" + urlNews + "'"
            conn = db_connection()
            cur = conn.cursor()
            cur.execute(statement)
            obj = cur.fetchall()
            conn.close()
        elif(obj[0][7] == destaques and obj[0][8] != ultimas):
            print("update ultimass")
            statement = " UPDATE news SET ultimas = " + ultimas + "WHERE url = '" + urlNews + "'"
            conn = db_connection()
            cur = conn.cursor()
            cur.execute(statement)
            obj = cur.fetchall()
            conn.close()

def getDataSN(r, classe, max, destaques, ultimas):
    information = r.html.xpath(classe)

    for i in range(0, max):
        urlImage = getInformation(information, i, "https:", '<img src="', 'mw-320"')
        if(urlImage == ""):
            urlImage = "/static/logosNews/sic.png"

        aux = getInformation(information, i, "", '<a href="', '" target')

        try:
            urlNews = "https://sicnoticias.pt" + aux
        except:
            urlNews = None

        try:
            category = aux.strip("/").split("/")[0]
        except:
            category = ""

        title = getInformation(information, i, "", 'rel="canonical"> ', '</a>')

        description = getInformation(information, i, "", '<h2 class="lead"> ', '</h2>')

        data = getInformation(information, i, "", 'datetime="', '" itemprop')

        if(data == ""):
            data = datetime.datetime.now()

        if(urlNews == "" or title == ""):
            pass
        else:
            addDB("SIC", urlNews, urlImage, title, description, data, category, destaques, ultimas)

def mainSN():
    '''Ultimas'''
    urlSN = "https://sicnoticias.pt/ultimas"
    r = createLink(urlSN, False)

    classe = '//*[@class="js-list-articles-entry entry-' #1 odd

    for i in range(1,11):
        aux = classe + str(i)
        if(i%2 == 0):
            aux = aux + ' even"]'
        else:
            aux = aux + ' odd"]'
        getDataSN(r, aux, 1, False, True)


    '''Destaques'''
    r = createLink("https://sicnoticias.pt/", False)

    for i in range(1,6):
        aux = classe + str(i)
        if(i%2 == 0):
            aux = aux + ' even"]'
        else:
            aux = aux + ' odd"]'
        getDataSN(r, aux, 2, True, False)

def getDataSapo(r, classe, pos, destaques, ultimas):
    meses = ["jan", "1", "fev", "2", "mar", "3", "abr", "4", "mai", "5", "jun", "6", "jul", "7", "ago", "8", "set", "9", "out", "10", "nov", "11", "dez", "12"]
    information = r.html.xpath(classe)

    urlImage = description = ""

    urlImage = getInformation(information, pos, "https://", 'data-original-src="//', '" t')

    aux = information[pos].html.split('<a href="')[1].split('" tabindex=')[0]

    if("class=" not in aux):

        urlNews = "https://24.sapo.pt" + aux

        category = aux.strip("/").split("/")[0]

        if(categorias in categorias):
            pass
        else:
            category = "Outras"

        title = information[pos].html.split('<span>')[1].split('</span>')[0]
        
        try:
            description = information[pos].html.split('<div class="[ quarter-top-space medium ] excerpt hide-tiny hide-small">')[1].split('</div>')[0]
        except:
            description = ""

        day = information[pos].html.split('"day">')[1].split('</span>')[0]
        month = information[pos].html.split('"month">')[1].split('</span>')[0]
        year = information[pos].html.split('"year">')[1].split('</span>')[0]
        hour = information[pos].html.split('"time">')[1].split('</span>')[0]

        for i in range(0, len(meses), 2):
            if(month == meses[i]):
                month = meses[i+1]

        dateStr = year + "-" + month + "-" + day + " " + hour
        data = datetime.datetime.strptime(dateStr, '%Y-%m-%d %H:%M')

        addDB("SAPO", urlNews, urlImage, title, description, data, category, destaques, ultimas)

def getDataRR(r, classe, pos):
    information = r.html.xpath(classe)
    print(information)
    urlImage = information[pos].html.split('<img data-src="')[1].split('alt=')[0]

    print(urlImage)

    """
    urlNews = "https://rr.sapo.pt" + information[pos].html.split('<a href="')[1].split('" tabindex=')[0]

    title = information[pos].html.split('<span>')[1].split('</span>')[0]
    description = ""
    try:
        description = information[pos].html.split('<div class="[ quarter-top-space medium ] excerpt hide-tiny hide-small">')[1].split('</div>')[0]
    except:
        description = ""

    day = information[pos].html.split('"day">')[1].split('</span>')[0]
    month = information[pos].html.split('"month">')[1].split('</span>')[0]
    year = information[pos].html.split('"year">')[1].split('</span>')[0]
    hour = information[pos].html.split('"time">')[1].split('</span>')[0]

    if(month == "jul"):
        month = "7"

    dateStr = year + "-" + month + "-" + day + " " + hour
    data = datetime.datetime.strptime(dateStr, '%Y-%m-%d %H:%M')

    return urlImage, urlNews, title, description, data
    """

def mainSapo():
    '''Ultimas'''
    urlSapo = "https://24.sapo.pt/ultimas"
    r = createLink(urlSapo, False)

    classe = '//*[@class="[ tiny-100 small-100 medium-33 large-33 xlarge-33 ]"]'

    for i in range(0,11):
        getDataSapo(r, classe, i, False, True)

    '''Destaques'''
    r = createLink("https://24.sapo.pt/", False)
    classe = '//*[@class="[ all-100 ]"]'

    for i in range(0,36):
        getDataSapo(r, classe, i, True, False)

def getDataMaisFutebol(r, classe, pos):
    information = r.html.xpath(classe)

    urlImage = getInformation(information, pos, "", '<div class="picture16x9" style="background-image: url(', '//);">')

    urlNews = information[pos].html.split('<a href="')[1].split('">')[0]

    title = information[pos].html.split('<h2 class="title">')[1].split('</h2>')[0]

    try:
        description = information[pos].html.split('class="relacionado">')[1].split('</a')[0]
    except:
        description = ""

    data = datetime.datetime.now()


    return urlImage, urlNews, title, description, data

def getDestaquesMaisFut():
    urlMaisFutebol = "https://maisfutebol.iol.pt"
    r = createLink(urlMaisFutebol, False)

    classe = '//*[@class="manchete mancheteNormal slide responsiveImg"]'

    for i in range(0,5):
        information = r.html.xpath(classe)

        try:
            urlImage = information[i].html.split('data-img="')[1].split('" sytle=')[0]
        except:
            urlImage = "/static/logosNews/maisfutebol.png"

        try:
            urlNews = information[i].html.split('<a href="')[1].split('" class="linkImgManchete"/>')[0]
        except:
            urlNews = None

        try:
            title = information[i].html.split('<a href="' + urlNews + '">')[1].split('<span>')[0].replace("\n","")
        except:
            title = None

        data = datetime.datetime.now()
        if(urlNews != None and title != None):
            addDB("Mais Futebol", urlNews, urlImage, title, "", data, "Desporto", True, True)

def mainMaisFutebol():
    '''Ultimas'''
    '''
    r = createLink("https://maisfutebol.iol.pt/ultimas", False)

    classe = '//*[@class="bigNewsList ultimasTimelineList"]'
    information = r.html.xpath(classe)
    print(information[0].html)
    
    for i in range(0,6):
        urlImage, urlNews, title, description, data = getDataMaisFutebol(r, classe, i)

        addDB("Mais Futebol", urlNews, urlImage, title, description, data, "Desporto", True, False)
    
    '''
    urlMaisFutebol = "https://maisfutebol.iol.pt"
    r = createLink(urlMaisFutebol, False)

    classe = '//*[@class="destaqueDiv"]'

    for i in range(0,6):
        urlImage, urlNews, title, description, data = getDataMaisFutebol(r, classe, i)

        addDB("Mais Futebol", urlNews, urlImage, title, description, data, "Desporto", True, False)
    '''Destaques'''
    getDestaquesMaisFut()

def getTSF(r, classe, pos):
    information = r.html.xpath(classe)

    urlImage = information[pos].html.split('data-src="')[1].split('" class')[0].replace("amp;","").replace("w=320&h=180&","")
    
    aux = information[pos].html.split('<a href="')[1].split('" class')[0]

    urlNews = "https://www.tsf.pt" + aux
    
    category = aux.strip("/").split("/")[0]

    title = information[pos].html.split('<span>')[1].split('</span>')[0]

    description = ""
    try:
        description = information[pos].html.split('<h4 class="t-am-lead"><span>')[1].split('</span>')[0]
    except:
        description = ""

    data = datetime.datetime.now()

    return urlImage, urlNews, title, description, data, category

def getTSFLast(r):
    information = r.html.find('article')

    for i in range(0, 15):
        urlImage = information[i].html.split('data-src="')[1].split('" class')[0].replace("amp;","").replace("w=320&h=180&","").replace("w=240&h=135&","")
        
        aux = information[i].html.split('<a href="')[1].split('" class')[0]

        urlNews = "https://www.tsf.pt" + aux
        
        category = aux.strip("/").split("/")[0]

        title = information[i].html.split('<span>')[1].split('</span>')[0]

        description = ""

        try:
            description = information[i].html.split('<h4 class="t-am-lead"><span>')[1].split('</span>')[0]
        except:
            description = ""

        data = datetime.datetime.now()

        addDB("TSF", urlNews, urlImage, title, description, data, category, False, True)

def mainTSF():
    '''Ultimas'''
    r = createLink("https://www.tsf.pt/ultimas.html", False)

    getTSFLast(r)


    '''Destaques'''
    r = createLink("https://www.tsf.pt/", False)

    classe = '//*[@class="t-s8-am2"]'

    for i in range(0,4):
        urlImage, urlNews, title, description, data, category = getTSF(r, classe, i)

        addDB("TSF", urlNews, urlImage, title, description, data, category, True, False)

def mainPPL():
    r = createLink("https://pplware.sapo.pt/", False)

    classe = '//*[@class="post-inner"]'
    information = r.html.xpath(classe)

    for i in range(0,len(information)):
        try:
            title = information[i].html.split('">')[3].split('</a>')[0]

            urlImage = information[i].html.split('<img loading="lazy" src="')[1].split('" alt=')[0]

            urlNews = information[i].html.split('<a target="_blank" href="')[1].split('" ')[0]

            data = information[i].html.split('time datetime="')[1].split('+')[0] + ".000Z"

            addDB("pplware", urlNews, urlImage, title, "", data, "Tecnologia", False, True)
        except:
            pass

def mainJornalCentro():
    r = createLink("https://www.jornaldocentro.pt/", False)

    classe = '//*[@class="post post-medium border-0 pb-0 mb-lg-4 mb-xl-5"]'
    information = r.html.xpath(classe)

    for i in information:
        try:
            urlNews = i.html.split('<a href="')[1].split('">')[0]

            title = i.html.split('<a class="text-dark" href="' + urlNews+ '">')[1].split('</a></h3>')[0].strip()

            urlImage = i.html.split('<img src="')[1].split('" class=')[0]

            data = i.html.split('<span class="light float-xl-right mt-xl-3 text-1 text-nowrap">')[1].split('</span>')[0]
            data = data.split(' ')
            dateStr = data[4].strip(',') + "-" + data[2] + "-" + data[0] + " " + data[5]
            data = datetime.datetime.strptime(dateStr, '%Y-%m-%d %H:%M')

            addDB("Jornal do Centro", urlNews, urlImage, title, "", data, "Centro", False, False)
        except:
            pass

def mainDiarioAlentejo():
    r = createLink("https://diariodoalentejo.pt/pt/noticias-listagem.aspx", False)
    meses = ["jan", "1", "fev", "2", "mar", "3", "abr", "4", "mai", "5", "jun", "6", "jul", "7", "ago", "8", "set", "9", "out", "10", "nov", "11", "dez", "12"]

    classe = '//*[@class="col-12 col-sm-6 col-md-4 col-lg-3 mb-3 px-2"]'
    information = r.html.xpath(classe)

    for i in information:
        try:
            urlNews = i.html.split('<a href="')[1].split('" target="')[0]
            urlNews = "https://diariodoalentejo.pt/" + urlNews

            aux = i.find("h2")[0].html
            title = aux.split('">')[2].split('</a></h2>')[0].strip()

            urlImage = i.html.split('data-src="')[1].split('" title="')[0].replace("w=260&amp;h=171&amp;","")
            urlImage = "https://diariodoalentejo.pt" + urlImage

            data = i.html.split('<span class="date">')[1].split('</span>')[0]
            data = data.split(' ')

            month = data[1]
            for i in range(0, len(meses), 2):
                if(month == meses[i]):
                    month = meses[i+1]

            dateStr = data[2] + "-" + month + "-" + data[0] + " " + data[3]
            data = datetime.datetime.strptime(dateStr, '%Y-%m-%d %H:%M')

            addDB("Diário do Alentejo", urlNews, urlImage, title, "", data, "Sul", False, False)
        except:
            pass

def mainOMinho():
    r = createLink("https://ominho.pt/", False)

    classe = '//*[@class="mvp-blog-story-wrap left relative infinite-post"]'
    information = r.html.xpath(classe)

    for i in information:
        try:
            urlNews = i.html.split('<a href="')[1].split('" rel="bookmark">')[0]

            title = i.html.split('<h2>')[1].split('</h2>')[0].strip()

            urlImage = i.html.split('data-lazy-srcset="//')[1].split(' 400w,')[0].replace("-400x240","")
            urlImage = "https://" + urlImage

            urlImage = "/static/logosNews/minho.png"

            data = datetime.datetime.now()

            addDB("O Minho", urlNews, urlImage, title, "", data, "Norte", False, False)
        except:
            pass

def mainOficial():
    while(True):
        mainSN()
        mainSapo()
        mainMaisFutebol()
        mainTSF()
        mainPPL()
        mainJornalCentro()
        time.sleep(300)

def main():
    mainSN()
    mainSapo()
    mainMaisFutebol()
    mainTSF()
    mainPPL()
    mainJornalCentro()
    mainDiarioAlentejo()
    mainOMinho()

#mainOficial()
main()

def getRazaoAutomovel():
    url = "https://www.razaoautomovel.com/categoria/noticias"
    r = createLink(url, False)

    classe = '//*[@class="card"]'

    for i in range(0,1):
        #urlImage, urlNews, title, description, data = getDataMaisFutebol(r, classe, i)
        information = r.html.xpath(classe)

        urlImage = information[i].html.split('src="')[1].split('" class=')[0].replace("-349x196","")
        
        urlNews = information[i].html.split('<a href="')[1].split('" title=')[0]

        title = information[i].html.split('<h5 class="title">')[1].split('</h5>')[0]

        data = datetime.datetime.now()

        addDB("Razão Automóvel", urlNews, urlImage, title, "", data, "Auto", True, True)

getRazaoAutomovel()