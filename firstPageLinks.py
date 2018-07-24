#-*- coding: utf-8 -*-

from splinter import Browser
import pandas as pd
import time


def firstSearches(search):
    hour = time.strftime("%H:%M:%S")
    date = time.strftime("%d/%m/%y")

    browser = Browser('chrome')
    browser.driver.set_window_size(640, 480)
    browser.visit('https://www.google.com')

    search_bar_xpath = '//*[@id="lst-ib"]'
    search_button_xpath = '//*[@id="tsf"]/div[2]/div[3]/center/input[1]'

    search_bar = browser.find_by_xpath(search_bar_xpath)[0]
    search_button = browser.find_by_xpath(search_button_xpath)[0]

    search_bar.fill(search)
    search_button.click()

    search_results_xpath = '//h3[@class="r"]/a'
    search_results = browser.find_by_xpath(search_results_xpath)
    for search_result in search_results:
        title = search_result.text.encode('utf8')
        link = search_result["href"]
        scraped_data.append((title, link))

    df = pd.DataFrame(data=scraped_data, columns=["Title", "Link"])
    df.to_csv("/home/enrique/Escritorio/links_" + date + "_" + hour + ".csv")


if __name__=="__main__":
    firstSearches('noticias ciencia')