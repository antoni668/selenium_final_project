from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure


class MainPage(Base):
    url = 'https://zlatoz.ru/'
    product_page_url = 'https://zlatoz.ru/catalog/nozhi_ukrashennye_/'
    email = 'apetrtest@mail.ru'
    password = 'Df64fT_'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    auth_block = '//*[@id="header"]//a[@data-name="auth"]'
    login_field = '//input[@id="USER_LOGIN_POPUP"]'
    password_field = '//input[@id="USER_PASSWORD_POPUP"]'
    login_button = '//button[normalize-space(span)="Войти"]'
    my_office = '//*[@id="header"]//span[normalize-space(span)="Мой кабинет"]/span'
    catalog = '//header[@id="header"]//a[contains(., "Каталог")]'
    product_menu_element = '//div[@class="burger_menu_wrapper"]//span[contains(text(), "Длинноклинковое")]'
    knives = '//header[@id="header"]//a[contains(., "Ножи украшенные")]'




    # Getters
    def get_auth_block(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.auth_block)))

    def get_username(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_field)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_my_office(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.my_office)))

    def get_catalog(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_product_menu_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.product_menu_element)))

    def get_knives(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.knives)))


    # Actions
    def click_auth_block(self):
        self.get_auth_block().click()
        print('auth block clicked')

    def input_username(self, username):
        self.get_username().send_keys(username)
        print('username entered')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('password entered')

    def click_login_button(self):
        self.get_login_button().click()
        print('login button clicked')

    def click_catalog(self):
        self.get_catalog().click()
        print('catalog clicked')

    def move_to_product_menu_element(self, actions):
        actions.move_to_element(self.get_product_menu_element()).perform()
        print('move to product menu element')

    def click_knives(self):
        self.get_knives().click()
        print('knives selected')


    # Methods
    def authorization(self):
        with allure.step('Authorization'):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_auth_block()
            self.input_username(self.email)
            self.input_password(self.password)
            self.click_login_button()
            self.assert_word(self.get_my_office(), "МОЙ КАБИНЕТ")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")

    def open_product_page(self):
        with allure.step('Open product page'):
            Logger.add_start_step(method="open_product_page")
            actions = ActionChains(self.driver)
            self.click_catalog()
            # self.move_to_product_menu_element(actions)
            self.click_knives()
            self.assert_url(self.product_page_url)
            Logger.add_end_step(url=self.driver.current_url, method="open_product_page")