from pages.temp_code_page import TempCodePage
import time


def test_phone_btn(selenium):        # Кнопка "Телефон"
    page = TempCodePage(selenium)
    page.phone_btn_click()
    time.sleep(3)


def test_temp_code_page(selenium):    # Авторизация: номер и пароль
    page = TempCodePage(selenium)
    page.enter_id("phone")
    page.enter_pass("password")
    time.sleep(3)


def test_standard_btn(selenium):    # Кнопка "Войти"
    page = TempCodePage(selenium)
    page.standard_btn_click()
    time.sleep(3)


def test_forgot_btn(selenium):     # Кнопка "Забыл пароль"
    page = TempCodePage(selenium)
    page.forgot_btn_click()


def test_enter_by_code_btn(selenium):   # Кнопка "Войти по временному коду"
    page = TempCodePage(selenium)
    page.enter_by_code_btn.click()
    time.sleep(3)
