#-*- coding: utf-8 -*-

from splinter import Browser
import pandas as pd
import time


def firstSearches(search):
    hour = time.strftime("%H:%M:%S")
    date = time.strftime("%d/%m/%y")
    date = date.replace('/','-')

    browser = Browser('chrome')
    browser.driver.set_window_size(640, 480)
    keyWords = search.split()
    query = ''
    for i in range(len(keyWords)):
        if i != len(keyWords) - 1:
            query = query + keyWords[i] + '+'
        else:
            query = query + keyWords[i]
    url = 'https://www.google.es/search?q=' + query
    browser.visit(url)

    search_results_xpath = '//h3[@class="r"]/a'
    search_results = browser.find_by_xpath(search_results_xpath)

    scraped_data = []
    for search_result in search_results:
        title = search_result.text.encode('utf8')
        link = search_result["href"]
        scraped_data.append((title, link))

    df = pd.DataFrame(data=scraped_data, columns=["Title", "Link"])
    df.to_csv('/home/enrique/Documentos/Busqueda automatica/links_' + date + '_' + hour + '.csv')


def firstScholarSearches(search):
    hour = time.strftime("%H:%M:%S")
    date = time.strftime("%d/%m/%y")
    date = date.replace('/','-')

    browser = Browser('chrome')
    browser.driver.set_window_size(640, 480)
    keyWords = search.split()
    query = ''
    for i in range(len(keyWords)):
        if i != len(keyWords) - 1:
            query = query + keyWords[i] + '+'
        else:
            query = query + keyWords[i]
    url = 'https://scholar.google.es/scholar?hl=es&as_sdt=0%2C5&as_ylo=2018&q=' + query + '&oq='
    browser.visit(url)

    search_results_xpath = '//h3[@class="gs_rt"]/a'
    search_results = browser.find_by_xpath(search_results_xpath)

    scraped_data = []
    for search_result in search_results:
        title = search_result.text.encode('utf8')
        link = search_result["href"]
        scraped_data.append((title, link))

    df = pd.DataFrame(data=scraped_data, columns=["Title", "Link"])
    df.to_csv('/home/enrique/Documentos/Busqueda automatica/linksScholar_'+ query + '_' + date + '_' + hour + '.csv')


if __name__=="__main__":
    firstScholarSearches('field theories of mind')