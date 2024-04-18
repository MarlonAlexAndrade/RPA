import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Configurações do Selenium para abrir o site e pegar a cotação do dólar
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=servico, options=chrome_options)

nav.get('https://www.melhorcambio.com/dolar-hoje')
nav.maximize_window()
sleep(2)
dolar_comercial = nav.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')
nav.quit()

# Configurações de e-mail
email_from = "@gmail.com"
email_to = "@gmail.com"
email_subject = "E-mail automático do Python"
email_body = f"Olá, a cotação do dólar hoje é {dolar_comercial}."

# Configurações do servidor SMTP do Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "@gmail.com"
smtp_password = "app key"

# Criar e configurar o e-mail
msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = email_to
msg['Subject'] = email_subject
msg.attach(MIMEText(email_body, 'plain'))

# Conectar-se ao servidor SMTP do Gmail e enviar o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(email_from, email_to, msg.as_string())

print("E-mail enviado com sucesso.")
