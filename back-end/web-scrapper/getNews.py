from requests_html import HTMLSession
from datetime import datetime
import requests
from dotenv import load_dotenv
import os

'''
Get the information
'''
def get_information(information, split1, split2):
    try:
        data = information.html.split(split1)[1].split(split2)[0]
    except:
        data = ""
    
    return data

'''
Get the session of the url
Return the response
'''
def get_session(url, sleep):
    response = HTMLSession().get(url)

    if(sleep == True):
        response.html.render(sleep = 1)
    #else:
        #response.html

    return response

'''
Razão Automóvel
Ultima Atualização: 26/07/2024
'''
def get_razao_automovel(session, headers):
    news_site = "Razão Automóvel"
    news_category = "Auto"

    url = "https://www.razaoautomovel.com/categoria/noticias"
    r = get_session(url, False)

    classe = '//*[contains(@class, "d-flex") and (contains(@class, "n-0") or contains(@class, "n-1") or contains(@class, "n-2")) and contains(@class, "col-sm-") and  contains(@class, "col-lg-") and contains(@class, "col-xl-")]'

    information = r.html.xpath(classe)
    for i in range(0, len(information)):
        url_image = information[i].html.split('data-lazy-srcset="')[1].split(' 925w, ')[0]
        
        url_news = information[i].html.split('<a href="')[1].split('" class=')[0]

        title = information[i].html.split(url_news + '">')[1].split('</a>')[0].strip()

        data = datetime.now()

        post_news((title, url_news, url_image, "", data, news_category, news_site), session, headers)

'''
Pplware
Ultima Atualização: 26/07/2024
'''
def get_ppl(session, headers):
    url = "https://pplware.sapo.pt/"
    news_site = "pplware"
    news_category = "Tecnologia"

    r = get_session(url, False)

    classe = '//*[@class="post-inner"]'
    information = r.html.xpath(classe)

    for i in range(0,len(information)):
        try:
            title = information[i].html.split('">')[3].split('</a>')[0]

            urlImage = information[i].html.split('<img loading="lazy" decoding="async" src="')[1].split('" alt=')[0]

            urlNews = information[i].html.split('<a target="_blank" href="')[1].split('" ')[0]

            data = information[i].html.split('time datetime="')[1].split('+')[0] + ".000Z"

            post_news((title, urlNews, urlImage, "", data, news_category, news_site), session, headers)
        except:
            pass

'''
Get the data from the news Sapo
'''
def get_data_sapo(data, session, headers):
    meses = ["jan", "1", "fev", "2", "mar", "3", "abr", "4", "mai", "5", "jun", "6", "jul", "7", "ago", "8", "set", "9", "out", "10", "nov", "11", "dez", "12"]
    url_image = description = ""
    aux = get_information(data, '<a href="', '" tabindex=')
    
    url_image = "https://" + get_information(data, 'data-original-src="//', '" t')

    url_news = "https://24.sapo.pt" + aux

    category = aux.strip("/").split("/")[0]
    category = category[0].upper() + category[1:]

    title = get_information(data, '<span>', '</span>')
        
    try:
        description = data.html.split('<div class="[ quarter-top-space medium ] excerpt hide-tiny hide-small">')[1].split('</div>')[0].strip()
    except:
        description = ""

    day = data.html.split('"day">')[1].split('</span>')[0]
    month = data.html.split('"month">')[1].split('</span>')[0]
    year = data.html.split('"year">')[1].split('</span>')[0]
    hour = data.html.split('"time">')[1].split('</span>')[0]

    for i in range(0, len(meses), 2):
        if(month == meses[i]):
            month = meses[i+1]

    date_str = year + "-" + month + "-" + day + " " + hour
    data = datetime.strptime(date_str, '%Y-%m-%d %H:%M')

    post_news((title, url_news, url_image, description, data, category, "Sapo"), session, headers)

def get_sapo_news(url, classe, session, headers):
    session = get_session(url, False)

    information = session.html.xpath(classe)

    for i in range(0, len(information)):
        get_data_sapo(information[i], session, headers)

'''
Sapo
Ultima Atualização: 26/07/2024
'''
def get_sapo(session, headers):
    '''Ultimas'''
    url_last_sapo = "https://24.sapo.pt/ultimas"
    classe = '//*[@class="[ tiny-100 small-100 medium-33 large-33 xlarge-33 ]"]'

    get_sapo_news(url_last_sapo, classe, session, headers)

    '''Destaques'''
    #url_tops_sapo = "https://24.sapo.pt/"
    #classe = '//*[@class="[ all-100 ]"]'

    #get_sapo_news(url_last_sapo, classe)

'''
Get the data from the news Mais Futebol
'''
def get_data_mais_futebol(session, headers):
    url_mais_futebol = "https://maisfutebol.iol.pt"
    session = get_session(url_mais_futebol, False)
    classe = '//*[@class="destaqueDiv"]'

    information = session.html.xpath(classe)

    for i in range(0, len(information)):
        url_image = get_information(information[i], '<div class="picture16x9" style="background-image: url(', '//);">')

        url_news = information[i].html.split('<a href="')[1].split('">')[0]

        try:
            title = information[i].html.split('<h2>')[1].split('</h2>')[0]
        except:
            title = information[i].html.split('<h2 class="title">')[1].split('</h2>')[0]

        try:
            description = information[i].html.split('class="relacionado">')[1].split('</a')[0]
        except:
            description = ""

        data = datetime.now()

        post_news((title, url_news, url_image, description, data, "Desporto", "Mais Futebol"), session, headers)

'''
Get the highlights from the news Mais Futebol
'''
def get_destaques_mais_fut(session, headers):
    url_mais_futebol = "https://maisfutebol.iol.pt"
    session = get_session(url_mais_futebol, False)

    classe = '//*[@class="manchete mancheteNormal slide responsiveImg"]'

    information = session.html.xpath(classe)
    for i in range(0, len(information)):
        try:
            url_image = information[i].html.split('data-img="')[1].split('" sytle=')[0]
        except:
            url_image = "/static/logosNews/maisfutebol.png"

        try:
            url_news = information[i].html.split('<a href="')[1].split('" class="linkImgManchete"/>')[0]
        except:
            url_news = None

        try:
            title = information[i].html.split('<a href="' + url_news + '">')[1].split('<span>')[0].replace("\n","")
        except:
            title = None

        data = datetime.now()
        if(url_news != None and title != None):
            post_news((title, url_news, url_image, "", data, "Desporto", "Mais Futebol"), session, headers)

'''
Mais Futebol
Ultima Atualização: 26/07/2024
'''
def get_mais_futebol(session, headers):
    '''Ultimas'''
    # To do

    '''Noticias'''
    get_data_mais_futebol(session, headers)

    '''Destaques'''
    get_destaques_mais_fut(session, headers)

'''
Sic Noticias
Ultima Atualização: 26/07/2024
'''
def get_sic_noticias(session, headers):
    '''Ultimas'''
    url_sic_noticias = "https://sicnoticias.pt/ultimas"
    session = get_session(url_sic_noticias, False)

    articles = session.html.xpath('//ul[contains(@class ,"list-articles item-count-12")]/descendant::li')

    for article in articles:
        title = article.html.split('_self"><span>')[1].split('</span></a>')[0].strip()
        url_news = "https://sicnoticias.pt" + article.html.split('<a href="')[1].split('"')[0]
        image_element = ""
        category = article.html.split('">')[7].split('</a></p>')[0].strip()
        date = datetime.now()

        description = article.html.split('>')[24].split('</')[0].strip()
        if("class" in description):
            description = ""
        
        post_news((title, url_news, image_element, description, date, category, "Sic Noticias"), session, headers)

'''
Login
'''
def login():
    load_dotenv(override=True)

    login_data = {
        'username': os.getenv('USERNAME'),
        'password': os.getenv('PASSWORD')
    }

    login_url = os.getenv('BASE_URL') + 'login/'

    session = requests.Session()

    # Login
    response = session.post(login_url, data=login_data)

    # Check if login was successful
    if response.status_code == 200 and response.json().get('token'):
        token = response.json().get('token')

        headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
        }

        return session, headers
    else:
        print("Error login:", response.status_code)
        return None

'''
Post the news
'''
def post_news(data, session, headers):
    load_dotenv(override=True)

    post_url = os.getenv('BASE_URL') + 'news/'

    post_data = {
        'title': data[0],
        'url': data[1],
        'image_url': data[2],
        'description': data[3],
        'datetime': data[4].isoformat() if isinstance(data[4], datetime) else data[4],
        #'category': data[5],
        #'site': data[6]
    }

    # POST
    post_response = session.post(post_url, json=post_data, headers=headers)

    if post_response.status_code != 201:
        print("Error POST:", post_response.status_code)
        print(post_response.json())

if __name__ == "__main__":
    session, headers = login()
    get_razao_automovel(session, headers)
    get_ppl(session, headers)
    get_sapo(session, headers)
    get_mais_futebol(session, headers)
    get_sic_noticias(session, headers)
