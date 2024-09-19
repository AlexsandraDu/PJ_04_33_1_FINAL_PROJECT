from pages.base_page import BasePage
import pages.locators
import pytest

#  Страница авторизации


class AuthPage(BasePage):

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        url = "http://b2c.passport.rt.ru"
        driver.get(url)   # Выставляем координаты тестируемых объектов:
        self.id = driver.find_element(*pages.locators.AuthLocators.AUTH_BUTTON)
        self.passw = driver.find_element(*pages.locators.AuthLocators.AUTH_PASSW)
        self.standard_btn = driver.find_element(*pages.locators.AuthLocators.STANDARD_BTN)
        self.forgot_btn = driver.find_element(*pages.locators.AuthLocators.FORGOT_BTN)
        self.register_btn = driver.find_element(*pages.locators.AuthLocators.REGISTER_BTN)
        self.login_btn = driver.find_element(*pages.locators.AuthLocators.LOGIN_BUTTON)
        self.email_btn = driver.find_element(*pages.locators.AuthLocators.EMAIL_BUTTON)
        self.account_btn = driver.find_element(*pages.locators.AuthLocators.ACCOUNT_BUTTON)
        self.phone_btn = driver.find_element(*pages.locators.AuthLocators.PHONE_BUTTON)

    # Ввод идентификатора в поле "Номер телефона". 
    @pytest.mark.parametrize("value", ["phone", "mail", "login", "account"])
    def enter_id(self, value):
        self.id.send_keys(value)

    def enter_pass(self, value):       # Ввод пароля
        self.passw.send_keys(value)

    def standard_btn_click(self):     # Кнопка "Войти"
        self.standard_btn.click()

    def forgot_btn_click(self):       # Кнопка "Забыл пароль"
        self.forgot_btn.click()

    def register_btn_click(self):      # Кнопка "Зарегистрироваться"
        self.register_btn.click()

    def email_btn_click(self):         # Кнопка "Почта"
        self.email_btn.click()

    def login_btn_click(self):        # Кнопка "Логин"
        self.login_btn.click()

    def account_btn_click(self):      # Кнопка "Лицевой счёт"
        self.account_btn.click()

    def phone_btn_click(self):        # Кнопка "Номер телефона"
        self.phone_btn.click()
