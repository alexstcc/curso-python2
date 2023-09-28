#import webbrowser

#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options

# Abrindo o navegador com webbrowser
#webbrowser.open('https://udeploy.sicredi.com.br/', autoraise=True)

#navegador = webdriver.Firefox()
#navegador.set_page_load_timeout(30)
#navegador.get('https://udeploy.sicredi.com.br/')

#navegador.find_element_by_id('usernameField').send_keys('alex_antonio')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

with webdriver.Firefox() as driver:

    driver.get('https://udeploy.sicredi.com.br/')
    wait = WebDriverWait(driver, 10)
    
    driver.find_element(By.NAME, "username").send_keys("alex_antonio" + Keys.RETURN)
    #wait.until(presence_of_element_located((By.XPATH, '//*[@id="usernameField"]')))
    
    driver.find_element(By.ID, "passwordField").send_keys("Ale04*sic" + Keys.RETURN)
    #wait.until(presence_of_element_located((By.XPATH, '//*[@id="passwordField"]')))

    driver.find_element(By.XPATH, "//*[@id='submitButton_label']").click()
    #wait.until(presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/form/div[4]/span/span')))