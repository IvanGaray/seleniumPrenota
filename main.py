from operator import truediv
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import schedule
import requests 

TOKEN = 'your bot Token'
goodEnding = "¡Pudes sacar turno!"
badEnging = "No hay turnos todavía."


chat_id = "your chat id"
message = "hello from your telegram bot"
#url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

def sendMessage(message):
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}").json()

class loginPrenota:
    def __init__(self, email:str, password:str):
        self.email = email
        self.password = password

usuario = loginPrenota('yourEmail','yourPassword')


def alert():

    chrome_options = Options()
    
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.create_options()
    driver.get("https://prenotami.esteri.it/")
    sleep(5)
    inputEmail = driver.find_element(By.CSS_SELECTOR,'input#login-email')
    inputEmail.send_keys(usuario.email)
    inputPassword = driver.find_element(By.CSS_SELECTOR,'input#login-password')
    inputPassword.send_keys(usuario.password)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,'button.button.primary.g-recaptcha').click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR,'a#advanced').click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR,'tbody > tr:nth-child(3) > td:nth-child(4) > a > button').click()
    sleep(3)
    if driver.find_element(By.XPATH,'//*[contains(text(), "momento non")]'):
        sendMessage(badEnging)
        driver.get('https://www.youtube.com/watch?v=BuLw2z8Jm98')
        sleep(10)     
    else:
        sendMessage(goodEnding)
        driver.get('https://www.youtube.com/watch?v=ZXsQAXx_ao0')
        sleep(5)
        #Finish the cycle
        return schedule.CancelJob

    driver.close()


#defining how often we will execute the function between 2 and 10 seconds.
schedule.every(2).to(10).seconds.do(alert)


while True:
    schedule.run_pending()
    sleep(600)

