from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def change_to_second_tab(self):
        new_page = self.driver.window_handles[1]
        return self.driver.switch_to.window(new_page)