import time
import allure
from selenium import webdriver
from pages.main_page import MainPage


@allure.description("Test buy product")
def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    print("Start Test")

    login = MainPage(driver)
    login.authorization()
    login.open_product_page()


    print("Finish Test")
    time.sleep(10)
    driver.quit()