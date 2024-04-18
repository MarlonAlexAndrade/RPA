from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=servico, options=chrome_options)

nav.get('http://www.google.com')

nav.maximize_window()

sleep(1)

nav.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('RPA', Keys.ENTER)

sleep(1)
nav.get_screenshot_as_file('rpa.png')

nav.quit()
