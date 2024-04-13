from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure


class ProductPage(Base):
    url = 'https://zlatoz.ru/catalog/nozhi_ukrashennye_/'
    cart_page_url = 'https://zlatoz.ru/basket/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product_availability = '//span[@title="Наличие в Златоусте"]'
    left_slider = '//a[@id="left_slider_c4ca4238a0b923820dcc509a6f75849b"]'
    right_slider = '//a[@id="right_slider_c4ca4238a0b923820dcc509a6f75849b"]'
    add_to_cart_button = '(//div[contains(@class, "footer_button")])[1]//i[@title="В корзину"]'
    cart_count = '//div[@class="pull-right"]//div[contains(@class, "top_basket")]//span[@class="count"]'
    clear_cart_button = '(//span[contains(@class, "remove_all_basket ")])[1]'
    cart = '//div[@class="pull-right"]//div[contains(@class, "top_basket")]//a'


    # Getters
    def get_product_availability(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.product_availability)))

    def get_left_slider(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.left_slider)))

    def get_right_slider(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.right_slider)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart_count(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_count)))

    def get_clear_cart_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.clear_cart_button)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))


    # Actions
    def click_product_availability(self):
        self.get_product_availability().click()
        print('click product availability')

    def click_and_hold_slider(self, action):
        action.click_and_hold(self.get_left_slider()).move_by_offset(10, 0).release().perform()
        action.click_and_hold(self.get_right_slider()).move_by_offset(-50, 0).release().perform()
        print('click and hold slider')

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print('click add to cart button')

    def click_cart(self):
        self.get_cart().click()
        print('click cart')


    # Methods

    # Очистить корзину если в ней есть товары
    def clear_cart(self, action):
        products_count = int(self.get_cart_count().text)
        if products_count > 0:
            action.move_to_element(self.get_cart()).perform()
            self.get_clear_cart_button().click()
            print('clear cart')

    # Обнаружил баг - не всегда рядом с пустой корзиной число равно 0
    def assert_cart_empty(self):
        assert int(self.get_cart_count().text) == 0
        print('cart is empty')

    def select_product(self):
        with allure.step('Select product'):
            Logger.add_start_step(method="select_product")
            actions = ActionChains(self.driver)
            self.get_current_url()
            self.click_product_availability()
            self.click_and_hold_slider(actions)
            self.clear_cart(actions)
            self.assert_cart_empty()
            self.click_add_to_cart_button()
            self.click_cart()
            self.assert_url(self.cart_page_url)
            Logger.add_end_step(url=self.driver.current_url, method="select_product")
