from utils.selenium_utils import init_driver, login, check_slots
from config import EMAIL, PASSWORD, RUCAPTCHA_KEY

def main():
    driver = init_driver()
    try:
        login(driver, EMAIL, PASSWORD, RUCAPTCHA_KEY)
        result = check_slots(driver)
        print(result)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
