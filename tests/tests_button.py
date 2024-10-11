from pages.button_page import ButtonPage


class TestButton:

    def test_button_click(self, browser):
        button_page = ButtonPage(browser, "https://demoqa.com/buttons")
        button_page.open()
        button_page.click_button()
        button_page.assert_text()
