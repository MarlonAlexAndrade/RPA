from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import pandas as pd
import io
import os

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=servico, options=chrome_options)

nav.get('https://rpachallengeocr.azurewebsites.net/')
nav.maximize_window()
sleep(1)

count_page = 1
while count_page <= 3:
    # Método Melhorado, sem nescessidade de criar arquivo
    tabela = nav.find_element(By.XPATH, '//*[@id="tableSandbox"]').get_attribute('innerText')

    tabela_io = io.StringIO(tabela)
    dados = pd.read_csv(tabela_io, delimiter='\t')

    tabela = nav.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    # Método usado no video
    # with open('Temp.csv', 'w') as file:
    #     file.write(tabela.text)
    # dados = pd.read_csv('Temp.csv')

    dados.to_csv('WebTable.csv', mode='a', index=None, header=(count_page == 1))

    nav.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    count_page += 1

nav.quit()
# os.remove('Temp.csv')

csv_xlsx = pd.read_csv('WebTable.csv')
csv_xlsx.to_excel('WebTable.xlsx', index=False)
