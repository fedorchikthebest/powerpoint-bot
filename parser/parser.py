from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep
import json
import os


options = Options()
options.page_load_strategy = 'eager'
prefs = {"download.default_directory" : f"{os.getcwd()}\\presentations\\", "directory_upgrade": True}
options.add_experimental_option("prefs",prefs)


def save_cookie(driver, path):
    with open(path, 'w') as filehandler:
        json.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
    with open(path, 'r') as cookiesfile:
        cookies = json.load(cookiesfile)
    for cookie in cookies:
        driver.add_cookie(cookie)


def login(email, password):
    global options
    '''Логинит пользователя по моему логину и паролю'''

    driver = webdriver.Chrome(options=options)

    try:
        load_cookie(driver, "parser/auth.json")
        return True
    except Exception:
        pass
    
    driver.get("https://id.freepik.com/v2/log-in?client_id=slidesgo&lang=en")

    sleep(10)
    
    e = driver.find_element(By.XPATH, '//*[@id="log-in"]/div[1]/button[2]')
    driver.execute_script("arguments[0].click();", e)

    sleep(10)

    email_elem = driver.find_element(By.NAME, "email")
    password_elem = driver.find_element(By.NAME, "password")


    email_elem.send_keys(email)
    password_elem.send_keys(password)
    password_elem.send_keys(Keys.RETURN)
    sleep(20)
    save_cookie(driver, "auth.json")
    driver.quit()


def generate_presentation(promt:str):
    global options
    '''Функция генерирует и сохраняет презентацию'''

    driver = webdriver.Chrome(options=options)

    driver.get('https://slidesgo.com/')

    load_cookie(driver, "parser/auth.json")

    driver.get('https://slidesgo.com/ai-presentations#from_element=main_menu')
    
    sleep(3)
        
    driver.find_element(By.XPATH, '//*[@id="landing-ai-cta"]').click()
    
    sleep(30)

    promt_input = driver.find_element(By.XPATH, '//*[@id="modal-ai-generator"]/div/div[1]/form/div[1]/div[1]/input')
    pages_input = driver.find_element(By.XPATH, '//*[@id="modal-ai-generator"]/div/div[1]/form/div[1]/div[2]/div[3]/input')
    
    pages_input.send_keys(Keys.DELETE)
    pages_input.send_keys("10")
    promt_input.send_keys(promt)
    promt_input.send_keys(Keys.RETURN)
    
    sleep(40)

    b = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/header/div/div[3]/div/div[1]/button')
    b.click()
    sleep(5)
    b = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/header/div/div[3]/div/div[1]/div/div/div[2]/button').click()
    sleep(40)
    driver.quit()