from pages.contacts_page import RedirectToTensor
from utils.utils import Utils

CURRENT_REGION = 'Ярославская обл.'
TEST_REGION = 'Камчатский край'

class TestPage:

    def test(self, driver):
        contact_page = RedirectToTensor(driver, 'https://www.sbis.ru/contacts')
        contact_page.open()

        assert contact_page.get_location_name() == CURRENT_REGION, 'Текущий регион не определился'
        assert Utils.check_elements_on_page(contact_page.is_partner_block_on_page()), 'Блок партнеров отсутствует'
        first_page_partners_block_name = contact_page.get_partners_block_name()

        contact_page.redirect_to_region_chose_page()
        contact_page.choose_41_region()

        assert contact_page.get_location_name() == TEST_REGION, 'Страница региона "Камчатский край" не загрузилась'
        assert first_page_partners_block_name != Utils.check_elements_on_page(contact_page.is_partner_block_on_page()), \
            'Блок партнеров не изменился'
        assert Utils.get_first_part_of_word(TEST_REGION) in driver.title, 'Название страницы не совпадает с тестовым'
        assert  Utils.get_lower_translit(Utils.get_first_part_of_word(TEST_REGION)) in driver.current_url.split('/')[-1], \
            'В URL не совпадает название региона'




