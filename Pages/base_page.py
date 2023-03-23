from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators, BasePageLocators
class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url) #для первого подхода перехода страниц

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def open(self):
        self.browser.get(self.url)

    def bool_returner(self, element, error = NoSuchElementException):
        try:
            element
        except error:
            return False
        return True

    def is_element_present(self, how, what):
        method = self.browser.find_element(how, what)
        return self.bool_returner(method)
    def is_word_in_url(self, word):
        method = word in self.browser.current_url
        return self.bool_returner(method)