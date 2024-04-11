from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):
    url = 'https://zlatoz.ru/'
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
        return WebDriverWait(self.driver, 992).until(
            EC.element_to_be_clickable((By.XPATH, self.my_office)))


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


    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_auth_block()
        self.input_username(self.email)
        self.input_password(self.password)
        self.click_login_button()
        self.assert_word(self.get_my_office(), "МОЙ КАБИНЕТ")
