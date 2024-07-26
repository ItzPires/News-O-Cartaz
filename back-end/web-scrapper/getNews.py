from requests_html import HTMLSession
import psycopg2
import sqlite3
import datetime
import time
import requests
from lxml import html

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

if __name__ == "__main__":
    get_razao_automovel()
    get_ppl()