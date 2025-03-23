

from pages.base_page import BasePage
from locators.tensor_about_page_locators import TensorAboutPageLocators

class TensorAboutPage(BasePage):
    locators = TensorAboutPageLocators()

    def find_pictures_on_people_power(self):
        return self.elements_is_visible(self.locators.PICTURES_ON_PEOPLE_POWER)