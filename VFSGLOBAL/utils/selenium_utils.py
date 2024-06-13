from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

from .captcha_solver import solve_captcha

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)

def login(driver, email, password, rucaptcha_key):
    driver.get("https://visa.vfsglobal.com/rus/ru/bgr/login")
    time.sleep(5)

    email_input = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    email_input.send_keys(email)
    password_input.send_keys(password)

    site_key = driver.find_element(By.CSS_SELECTOR, '.g-recaptcha').get_attribute('data-sitekey')
    captcha_solution = solve_captcha(rucaptcha_key, site_key, driver.current_url)
    
    wait = WebDriverWait(driver, 5)
    try:
        input_element = wait.until(EC.presence_of_element_located((By.NAME, "cf-turnstile-response")))
        driver.execute_script("arguments[0].value = arguments[1];", input_element, captcha_solution)
    except Exception as e:
        logging.error("Ошибка:", e)
    
    driver.find_element(By.CSS_SELECTOR, '#recaptcha-demo-submit').click()
    time.sleep(10)  # Ожидание загрузки страницы после входа

def check_slots(driver):
    driver.find_element(By.CSS_SELECTOR, 'a[href*="appointment"]').click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, 'select[id="visa_center"]').send_keys('Bulgaria VAC in Russia – Moscow')
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'select[id="category"]').send_keys('Short Stay')
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'select[id="subcategory"]').send_keys('Passport Submission')
    time.sleep(2)
    
    driver.find_element(By.CSS_SELECTOR, 'button[id="check_slots_button"]').click()
    time.sleep(5)
    
    result = driver.find_element(By.CSS_SELECTOR, 'div[id="slot_results"]').text
    return result
