from selenium.common.exceptions import NoSuchElementException

class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

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