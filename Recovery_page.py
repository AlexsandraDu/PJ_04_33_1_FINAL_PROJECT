from pages.base_page import BasePage
import pages.locators
import time
import pytest
# Страница "Восстановление пароля"

class RecoveryPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = ("https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=lk_b2c&tab_id=yKvcXQigVV4"
               "_id=account_b2c&tab_id=KQ1mz2Boq_U")
        driver.get(url)
        self.id = driver.find_element(*pages.locators.AuthLocators.AUTH_BUTTON)
        self.phone_btn = driver.find_element(*pages.locators.AuthLocators.PHONE_BUTTON)
        self.proceed_btn = driver.find_element(*pages.locators.AuthLocators.PROCEED_BUTTON)
        self.return_btn = driver.find_element(*pages.locators.AuthLocators.RETURN_BUTTON)
        self.captcha_reload = driver.find_element(*pages.locators.AuthLocators.CAPTCHA)
      
    def phone_btn_click(self):   # Кнопка "Телефон"
        self.phone_btn.click()

    @pytest.mark.parametrize("value", ["phone", "mail", "login", "account"])
    def enter_id(self, value):
        self.id.send_keys(value)     # Ввод любого идентификатора

    def proceed_btn_click(self):     # Кнопка "Продолжить"
        self.proceed_btn.click()
        time.sleep(3)

    def captcha_reload_click(self):     # Перезагрузка "капчи"
        self.captcha_reload.click()
        self.driver.implicitly_wait(1)

    def return_btn_click(self):      # Кнопка "Вернуться назад"
        self.return_btn.click()
