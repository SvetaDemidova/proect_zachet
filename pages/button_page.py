from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ButtonPage(BasePage):
    def click_button(self):
        self.browser.find_element(By.XPATH, '//button[text()="Click Me"]').click()

    def assert_text(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//p[text()="You have done a dynamic click"]')))