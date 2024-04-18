from time import sleep
import pyautogui as p
import pandas as pd
import requests
import os


# # p.PAUSE = 1
# # p.doubleClick(48, 224)
# # # p.hotkey('win', 'up')

os.system('start chrome --start-maximized')
sleep(2)
p.write('http://rpachallenge.com')
p.press('enter')

url = 'https://rpachallenge.com/assets/downloadFiles/challenge.xlsx'

caminho_arquivo = 'challenge.xlsx'

response = requests.get(url)

with open(caminho_arquivo, 'wb') as file:
    file.write(response.content)

dados = pd.read_excel('challenge.xlsx', sheet_name='Sheet1')
df = pd.DataFrame(dados, columns=["First Name", "Last Name ", "Company Name", "Role in Company", "Address", "Email", "Phone Number"])

p.click(236, 874)

p.PAUSE = 0.04
for row in df.itertuples():
    first_name = p.locateCenterOnScreen('Imagens_challenger/first_name.png', confidence=0.85, minSearchTime=5)
    p.moveTo(first_name.x, first_name.y+25)
    p.click()
    p.typewrite(row[1]  , interval=0.0001)

    last_name = p.locateCenterOnScreen('Imagens_challenger/last_name.png', confidence=0.85, minSearchTime=5)
    p.moveTo(last_name.x, last_name.y+25)
    p.click()
    p.typewrite(row[2]  , interval=0.0001)

    company_name = p.locateCenterOnScreen('Imagens_challenger/company_name.png', confidence=0.85, minSearchTime=5)
    p.moveTo(company_name.x, company_name.y+25)
    p.click()
    p.typewrite(row[3]  , interval=0.0001)

    role_in_company = p.locateCenterOnScreen('Imagens_challenger/role_in_company.png', confidence=0.85, minSearchTime=5)
    p.moveTo(role_in_company.x, role_in_company.y+25)
    p.click()
    p.typewrite(row[4]  , interval=0.0001)

    address = p.locateCenterOnScreen('Imagens_challenger/address.png', confidence=0.85, minSearchTime=5)
    p.moveTo(address.x, address.y+25)
    p.click()
    p.typewrite(row[5]  , interval=0.0001)

    email = p.locateCenterOnScreen('Imagens_challenger/email.png', confidence=0.85, minSearchTime=5)
    p.moveTo(email.x, email.y+25)
    p.click()
    p.typewrite(row[6]  , interval=0.0001)

    phone_number = p.locateCenterOnScreen('Imagens_challenger/phone_number.png', confidence=0.85, minSearchTime=5)
    p.moveTo(phone_number.x, phone_number.y+25)
    p.click()
    p.typewrite(str(row[7])  , interval=0.0001)
    
    submit = p.locateCenterOnScreen('Imagens_challenger/submit.png', confidence=0.85, minSearchTime=5)
    p.moveTo(submit.x, submit.y)
    p.click()
