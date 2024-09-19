from pages.recovery_page import RecoveryPage
import time


def test_phone_btn(selenium):      # Кнопка "Телефон"
    page = RecoveryPage(selenium)
    page.phone_btn.click()
    time.sleep(3)


def test_recovery_page(selenium):    # Ввести номер телефона и нажать кнопку "Продолжить"
    page = RecoveryPage(selenium)
    page.enter_id("phone")
    page.proceed_btn_click()
    time.sleep(3)


def test_captcha_reload(selenium):     # Перезагрузка "капчи"
    page = RecoveryPage(selenium)
    page.captcha_reload_click()


def test_return_btn(selenium):       # Кнопка "Вернуться назад"
    page = RecoveryPage(selenium)
    page.return_btn_click()
    time.sleep(3)
