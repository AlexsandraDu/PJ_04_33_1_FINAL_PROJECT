from selenium.webdriver.common.by import By

class AuthLocators:
    AUTH_BUTTON = (By.ID, "username")
    STANDARD_BTN = (By.ID, "kc-login")
    AUTH_PASSW = (By.ID, "password")
    EMAIL_BUTTON = (By.ID, "t-btn-tab-mail")
    FORGOT_BTN = (By.ID, "forgot_password")
    REGISTER_BTN = (By.ID, "kc-register")
    PHONE_BUTTON = (By.ID, "t-btn-tab-phone")
    LOGIN_BUTTON = (By.ID, "t-btn-tab-login")
    ACCOUNT_BUTTON = (By.ID, "t-btn-tab-ls")
    PROCEED_BUTTON = (By.ID, "reset")
    RETURN_BUTTON = (By.ID, "reset-back")
    ENTER_BY_CODE_BUTTON = (By.ID, "back_to_otp_btn")
    CAPTCHA = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div[1]/div[2]')
