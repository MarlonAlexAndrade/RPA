from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import pyautogui as p
import pandas as pd
import requests

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=servico, options=chrome_options)

nav.get('http://rpachallenge.com')
nav.maximize_window()
sleep(0.2)

url = 'https://rpachallenge.com/assets/downloadFiles/challenge.xlsx'

caminho_arquivo = 'challenge.xlsx'

response = requests.get(url)

with open(caminho_arquivo, 'wb') as file:
    file.write(response.content)

dados = pd.read_excel('challenge.xlsx', sheet_name='Sheet1')

df = pd.DataFrame(dados, columns=["First Name", "Last Name ", "Company Name", "Role in Company", "Address", "Email", "Phone Number"])

nav.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()

for row in df.itertuples():
    nav.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelFirstName"]').send_keys(row[1])
    nav.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelLastName"]').send_keys(row[2])
    nav.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelCompanyName"]').send_keys(row[3])
    nav.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelRole"]').send_keys(row[4])
    nav.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelAddress"]').send_keys(row[5])
    nav.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelEmail"]').send_keys(row[6])
    
    nav.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelPhone"]').send_keys(str(row[7]))
  
    nav.find_element(By.CSS_SELECTOR, 'input.btn.uiColorButton[type="submit"]').click()

p.screenshot('score.png')

nav.quit()
