from pages.base_page import BasePage
import pages.locators
import pytest

# Страница "Авторизация"с полем "Войти по временному коду"


class TempCodePage(BasePage):

    def __init__(self, driver, timeout=10):   # Координаты тестируемых объектов:
        super().__init__(driver, timeout)
        url = "https://my.rt.ru/"
        driver.get(url)
        self.id = driver.find_element(*pages.locators.AuthLocators.AUTH_BUTTON)
        self.passw = driver.find_element(*pages.locators.AuthLocators.AUTH_PASSW)
        self.phone_btn = driver.find_element(*pages.locators.AuthLocators.PHONE_BUTTON)
        self.standard_btn = driver.find_element(*pages.locators.AuthLocators.STANDARD_BTN)
        self.enter_by_code_btn = driver.find_element(*pages.locators.AuthLocators.ENTER_BY_CODE_BUTTON)
        self.forgot_btn = driver.find_element(*pages.locators.AuthLocators.FORGOT_BTN)

    def phone_btn_click(self):   # Кнопка "Телефон"
        self.phone_btn.click()

    @pytest.mark.parametrize("value", ["phone", "mail", "login", "account"])
    def enter_id(self, value):
        self.id.send_keys(value)    # Ввод идентификатора

    def enter_pass(self, value):     # Ввод пароля
        self.passw.send_keys(value)

    def standard_btn_click(self):    # Кнопка "Войти"
        self.standard_btn.click()

    def forgot_btn_click(self):      # Кнопка "Забыл пароль"
        self.forgot_btn.click()

    def enter_by_code_btn_click(self):    # Кнопка "Войти по временному коду"
        self.enter_by_code_btn.click()
