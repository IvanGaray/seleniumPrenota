from operator import truediv
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import schedule
import requests 
from credenciales import usuario,chat_id,TOKEN,hayTurno,noHayTurno,loginPrenota


def sendMessage(message):
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}").json()


def alert():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.create_options()
    driver.get("https://prenotami.esteri.it/")
    sleep(5)
    inputEmail = driver.find_element(By.CSS_SELECTOR,'input#login-email')
    inputEmail.send_keys(usuario.email)
    inputPassword = driver.find_element(By.CSS_SELECTOR,'input#login-password')
    inputPassword.send_keys(usuario.password)
    sleep(3)
    driver.find_element(By.CSS_SELECTOR,'button.button.primary.g-recaptcha').click()
    sleep(5)
    driver.find_element(By.CSS_SELECTOR,'a#advanced').click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR,'tbody > tr:nth-child(3) > td:nth-child(4) > a > button').click()
    sleep(3)
    if driver.find_element(By.XPATH,'//*[contains(text(), "momento non")]'):
        try:
            sendMessage(noHayTurno)
        except Exception:
            print(Exception)
        
    else:
        try:
            sendMessage(hayTurno)
            return schedule.CancelJob
        except Exception:
            print(Exception)
        #Finish the cycle
        
    driver.close()

#defining how often we will execute the function between 600 and 1200 seconds.(10 to 20 minutes)
schedule.every(600).to(1200).seconds.do(alert)

while True:
    schedule.run_pending()
    sleep(2)

