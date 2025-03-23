from selenium.common.exceptions import NoSuchElementException
from transliterate import translit, get_available_language_codes

class Utils:

    def equal_pict_sizes(picts):
        image_sizes = []
        for img in picts[:4]:
            size = img.size
            image_sizes.append(size)

        for i in range(1, len(image_sizes)):
            assert image_sizes[i] == image_sizes[0], f"Размеры изображений не совпадают"

    def check_elements_on_page(self):
        try:
            self
        except NoSuchElementException:
            return False
        return True

    def get_first_part_of_word(self:str):
        return self.split()[0]

    def get_lower_translit(self):
        return translit(self, "ru", True).lower()