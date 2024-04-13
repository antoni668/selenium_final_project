import time
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.product_page import ProductPage


@allure.description("Test buy product")
def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    print("Start Test")

    main = MainPage(driver)
    main.authorization()
    main.open_product_page()

    prod = ProductPage(driver)
    prod.select_product()


    print("Finish Test")
    time.sleep(10)
    driver.quit()