import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

url = 'https://sol.sbc.org.br/journals/index.php/isys/issue/archive'

option = Options()
option.headless = True
driver = webdriver.Chrome(executable_path=r"C:\Users\dirce\Downloads\chromedriver_win32\chromedriver.exe")

driver.get(url)

#driver.find_element_by_xpath("//div[@class='obj_issue_summary']//h2//a[@class='title']").click()

html_list = driver.find_element_by_xpath("//ul[@class='issues_archive']")
items = html_list.find_element_by_xpath("//a[@class='title']")

urls = [i.get_attribute("href") for i in items]
nameOfArticles = []

for url in urls:
    #print (url)
    driver.get(url)
    master_list = driver.find_element_by_xpath("//ul[@class='cmp_article_list articles']")
    
    nameOfArticles = nameOfArticles + [i.text for i in master_list.find_elements_by_xpath("//h3[@class='title']//a")]
    driver.back()

f = open('articles_list.csv', 'w')

# write a row to the csv file
for articleName in nameOfArticles:
    f.write(articleName.encode('utf-8').replace(',','') + ','+ "\n")
f.close()
#driver.find_element_by_xpath("//div[@class='obj_issue_summary']//h2//a[@class='title']").click()

#

#driver. quit()

