class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self, endpoint=""):
        self.browser.get(self.url+endpoint)
