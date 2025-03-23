from locators.tensor_page_locators import TensorPageBanner
from pages.base_page import BasePage


class RedirectionToMoreInPeoplePower(BasePage):
    locators = TensorPageBanner()

    def redirect_to_more(self):
        self.element_is_visible(self.locators.BUTTON).click()

    def check_people_power_block(self):
        self.element_is_visible(self.locators.PEOPLE_POWER_BLANK)