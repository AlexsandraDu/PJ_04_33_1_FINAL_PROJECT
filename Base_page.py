from urllib.parse import urlparse

class BasePage(object):
    # конструктор класса - метод с ключевым словом __init__
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path
