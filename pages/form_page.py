from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage(BasePage):
    def add_records_text_form(self):
        self.browser.find_element(By.XPATH, '//*[@placeholder="Full Name"]').send_keys("Ivanov Ivan")
        self.browser.find_element(By.XPATH, '//*[@placeholder="name@example.com"]').send_keys("iv@mail.ru")
        self.browser.find_element(By.XPATH, '//*[@placeholder="Current Address"]').send_keys("Russia")
        self.browser.find_element(By.XPATH, '//*[@id="permanentAddress"]').send_keys("RF")
        self.browser.find_element(By.XPATH, '//*[@id="submit"]').click()

    def assert_text_in_form(self):

        WebDriverWait(self.browser, 5).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="name"]'),"Ivanov Ivan"))
        WebDriverWait(self.browser, 5).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="email"]'),"iv@mail.ru"))
        WebDriverWait(self.browser, 5).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="output"]'),"Russia"))
        WebDriverWait(self.browser, 5).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="output"]'),"RF"))