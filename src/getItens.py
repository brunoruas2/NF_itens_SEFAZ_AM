# -*- coding: utf-8 -*-
import sys
import time
import pandas as pd
import urllib.request

from selenium import webdriver

pd.options.mode.chained_assignment = None  # default='warn'

sys.path.insert(0, r'src\modules')
from popUpImg import showPopUp

# click function
def click(xpath):
  xpath = driver.find_element_by_xpath(xpath)
  xpath.click()

# send keys
def send_keys(xpath,keys):
  xpath = driver.find_element_by_xpath(xpath)
  xpath.send_keys(keys)

# clear element
def clear_elem(xpath):
  xpath = driver.find_element_by_xpath(xpath)
  xpath.clear()

## SCRAPING PART ##
driver = webdriver.Chrome(r"src\modules\webdriver\chromedriver.exe")
driver.maximize_window()

notaCode = input("Por favor, insira a chave de acesso da nota fiscal desejada\n\nCódigo:  ")

driver.get('https://sistemas.sefaz.am.gov.br/nfceweb/consultarNFCe.do?acao=submitConsultaNFCeRedirect&txtChaveAcessoNFe={}&hash=null'.format(notaCode))

time.sleep(5)

send_keys(xpath='//*[@id="txtChaveAcessoNFe"]',keys=notaCode)

# get the image https://stackoverflow.com/questions/49627458/python-selenium-download-images-jpeg-png-or-pdf-using-chromedriver
img = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[1]/td/table[1]/tbody/tr[1]/td/form/table/tbody/tr[1]/td[2]/img')
src = img.get_attribute('src') 
urllib.request.urlretrieve(src, "src\img\captcha.jpg")

captcha = input(showPopUp(path='src\img\captcha.jpg'))