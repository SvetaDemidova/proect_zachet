from pages.form_page import FormPage


class TestForm:

    def test_form(self, browser):
        form_page = FormPage(browser, "https://demoqa.com/text-box")
        form_page.open()
        form_page.add_records_text_form()
        form_page.assert_text_in_form()
