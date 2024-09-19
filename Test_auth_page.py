from pages.auth_page import AuthPage
import time


def test_auth(selenium):         # Авторизация
    page = AuthPage(selenium)
    page.enter_id("phone")
    page.enter_pass("password")
    page.standard_btn_click()


def test_forgot_password(selenium):      # Кнопка "Забыл пароль"
    page = AuthPage(selenium)
    page.enter_id("phone")
    page.forgot_btn_click()
    time.sleep(3)


def test_register_button(selenium):       # Кнопка "Зарегистрироваться"
    page = AuthPage(selenium)
    page.register_btn_click()
    time.sleep(3)


def test_mail_button(selenium):         # Кнопка "Почта"
    page = AuthPage(selenium)
    page.email_btn_click()
    time.sleep(3)


def test_login_button(selenium):        # Кнопка "Логин"
    page = AuthPage(selenium)
    page.login_btn_click()
    time.sleep(3)


def test_account_button(selenium):       # Кнопка "Лицевой счет"
    page = AuthPage(selenium)
    page.account_btn_click()
    time.sleep(3)


def test_phone_button(selenium):        # Кнопка "Номер телефона"
    page = AuthPage(selenium)
    page.phone_btn_click()
    time.sleep(3)
