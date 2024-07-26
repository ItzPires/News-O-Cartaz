from requests_html import HTMLSession
import psycopg2
import sqlite3
import datetime
import time
import requests
from lxml import html

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
def get_razao_automovel():
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

        data = datetime.datetime.now()

        #addDB(news_site, url_news, url_image, title, "", data, news_category, True, True)
        print(url_image, url_news, title, data)

'''
Pplware
Ultima Atualização: 26/07/2024
'''
def get_ppl():
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

            #addDB(news_site, urlNews, urlImage, title, "", data, news_category, False, True)
        except:
            pass

'''
Get the data from the news Sapo
'''
def get_data_sapo(news):
    meses = ["jan", "1", "fev", "2", "mar", "3", "abr", "4", "mai", "5", "jun", "6", "jul", "7", "ago", "8", "set", "9", "out", "10", "nov", "11", "dez", "12"]
    url_image = description = ""
    aux = get_information(news, '<a href="', '" tabindex=')
    
    url_image = "https://" + get_information(news, 'data-original-src="//', '" t')

    url_news = "https://24.sapo.pt" + aux

    category = aux.strip("/").split("/")[0]
    category = category[0].upper() + category[1:]

    title = get_information(news, '<span>', '</span>')
        
    try:
        description = news.html.split('<div class="[ quarter-top-space medium ] excerpt hide-tiny hide-small">')[1].split('</div>')[0].strip()
    except:
        description = ""

    day = news.html.split('"day">')[1].split('</span>')[0]
    month = news.html.split('"month">')[1].split('</span>')[0]
    year = news.html.split('"year">')[1].split('</span>')[0]
    hour = news.html.split('"time">')[1].split('</span>')[0]

    for i in range(0, len(meses), 2):
        if(month == meses[i]):
            month = meses[i+1]

    date_str = year + "-" + month + "-" + day + " " + hour
    data = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M')

    print(url_image, url_news, title, description, data, category)

def get_sapo_news(url, classe):
    session = get_session(url, False)

    information = session.html.xpath(classe)

    for i in range(0, len(information)):
        get_data_sapo(information[i])

'''
Sapo
Ultima Atualização: 26/07/2024
'''
def get_sapo():
    '''Ultimas'''
    url_last_sapo = "https://24.sapo.pt/ultimas"
    classe = '//*[@class="[ tiny-100 small-100 medium-33 large-33 xlarge-33 ]"]'

    get_sapo_news(url_last_sapo, classe)

    '''Destaques'''
    #url_tops_sapo = "https://24.sapo.pt/"
    #classe = '//*[@class="[ all-100 ]"]'

    #get_sapo_news(url_last_sapo, classe)

'''
Get the data from the news Mais Futebol
'''
def get_data_mais_futebol():
    url_mais_futebol = "https://maisfutebol.iol.pt"
    session = get_session(url_mais_futebol, False)
    classe = '//*[@class="destaqueDiv"]'

    information = session.html.xpath(classe)

    for i in range(0, len(information)):
        url_image = get_information(information[i], '<div class="picture16x9" style="background-image: url(', '//);">')

        url_news = information[i].html.split('<a href="')[1].split('">')[0]

        title = information[i].html.split('<h2 class="title">')[1].split('</h2>')[0]

        try:
            description = information[i].html.split('class="relacionado">')[1].split('</a')[0]
        except:
            description = ""

        data = datetime.datetime.now()

        #addDB("Mais Futebol", url_news, url_image, title, description, data, "Desporto", True, True)
        print(url_image, url_news, title, description, data)

'''
Get the highlights from the news Mais Futebol
'''
def get_destaques_mais_fut():
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

        data = datetime.datetime.now()
        if(url_news != None and title != None):
            #addDB("Mais Futebol", urlNews, urlImage, title, "", data, "Desporto", True, True)
            print(url_image, url_news, title, data)

'''
Mais Futebol
Ultima Atualização: 26/07/2024
'''
def get_mais_futebol():
    '''Ultimas'''
    # To do

    '''Noticias'''
    get_data_mais_futebol()

    '''Destaques'''
    get_destaques_mais_fut()

'''
Sic Noticias
Ultima Atualização: 26/07/2024
'''
def get_sic_noticias():
    '''Ultimas'''
    url_sic_noticias = "https://sicnoticias.pt/ultimas"
    session = get_session(url_sic_noticias, False)

    articles = session.html.xpath('//ul[contains(@class ,"list-articles item-count-12")]/descendant::li')

    for article in articles:
        title = article.html.split('_self"><span>')[1].split('</span></a>')[0].strip()
        url_news = "https://sicnoticias.pt" + article.html.split('<a href="')[1].split('"')[0]
        image_element = ""
        category = article.html.split('">')[7].split('</a></p>')[0].strip()
        date = datetime.datetime.now()

        description = article.html.split('>')[24].split('</')[0].strip()
        if("class" in description):
            description = ""
        
        print(title, url_news, category, date, description)


if __name__ == "__main__":
    get_razao_automovel()
    get_ppl()
    get_sapo()
    get_mais_futebol()
    get_sic_noticias()
