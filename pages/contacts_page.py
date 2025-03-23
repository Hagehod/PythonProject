from time import sleep

from locators.contacts_page_locators import TensorBannerLocators
from pages.base_page import BasePage


class RedirectToTensor(BasePage):
    locators = TensorBannerLocators()

    def redirect_to_tensor_banner(self):
        self.element_is_visible(self.locators.BANNER).click()

    def redirect_to_region_chose_page(self):
        self.element_is_visible(self.locators.REGION).click()

    def get_location_name(self):
        return self.element_is_visible(self.locators.REGION).text

    def is_partner_block_on_page(self):
        self.element_is_visible(self.locators.PARTNERS_BLOCK)

    def get_partners_block_name(self):
        return self.element_is_visible(self.locators.PARTNERS_BLOCK).text

    def choose_41_region(self):
        self.element_is_visible(self.locators.REGION_41).click()
        sleep(1)

    def get_title_name(self):
        return self.element_is_visible(self.locators.TITLE_NAME).text