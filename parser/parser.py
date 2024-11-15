from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import asyncio
import json


options = Options()
options.page_load_strategy = 'eager'
prefs = {"download.default_directory" : "D:\\Projects\\powerpoint-bot\\presentations", "directory_upgrade": True}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=options)


def save_cookie(driver, path):
    with open(path, 'w') as filehandler:
        json.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
    with open(path, 'r') as cookiesfile:
        cookies = json.load(cookiesfile)
    for cookie in cookies:
        driver.add_cookie(cookie)


async def login(email, password):
    '''Логинит пользователя по моему логину и паролю'''
    try:
        load_cookie(driver, "auth.json")
        return True
    except Exception:
        pass
    
    driver.get("https://id.freepik.com/v2/log-in?client_id=slidesgo&lang=en")

    await asyncio.sleep(3)
    
    driver.find_element(By.XPATH, "//*[@id=\"log-in\"]/div[1]/button[2]").click()

    await asyncio.sleep(3)

    email_elem = driver.find_element(By.NAME, "email")
    password_elem = driver.find_element(By.NAME, "password")


    email_elem.send_keys(email)
    password_elem.send_keys(password)
    password_elem.send_keys(Keys.RETURN)
    await asyncio.sleep(3)
    save_cookie(driver, "auth.json")


async def generate_presentation(promt:str):
    '''Функция генерирует и сохраняет презентацию'''
    
    driver.get('https://slidesgo.com/ai-presentations#from_element=main_menu')
    
    await asyncio.sleep(3)
        
    driver.find_element(By.XPATH, '//*[@id="landing-ai-cta"]').click()

    promt_input = driver.find_element(By.XPATH, '//*[@id="modal-ai-generator"]/div/div[1]/form/div[1]/div[1]/input')
    promt_input.send_keys(promt)
    promt_input.send_keys(Keys.RETURN)
    
    await asyncio.sleep(40)

    b = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/header/div/div[3]/div/div[1]/button')
    b.click()
    await asyncio.sleep(5)
    b = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/header/div/div[3]/div/div[1]/div/div/div[2]/button')
    b.click()
    await asyncio.sleep(40)


async def main(PROMT):
    driver.get("https://slidesgo.com")
    await login("")
    load_cookie(driver, "auth.json")
    await generate_presentation(PROMT)


