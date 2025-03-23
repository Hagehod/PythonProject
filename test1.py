from pages.contacts_page import RedirectToTensor
from pages.tensor_page import RedirectionToMoreInPeoplePower
from pages.tensor_about_page import TensorAboutPage
from utils.utils import Utils


class TestPage:

    def test(self, driver):
        form_page = RedirectToTensor(driver, 'https://www.sbis.ru/contacts')
        form_page.open()

        form_page.redirect_to_tensor_banner()
        form_page.change_to_second_tab()

        tensor_page = RedirectionToMoreInPeoplePower(driver, driver.current_url)
        assert Utils.check_elements_on_page(tensor_page.check_people_power_block()), 'Блок "Сила в людях" отсутствует'

        tensor_page.redirect_to_more()
        tensor_about_page = TensorAboutPage(driver, driver.current_url)

        images = tensor_about_page.find_pictures_on_people_power()
        Utils.equal_pict_sizes(images)