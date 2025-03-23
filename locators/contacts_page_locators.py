from selenium.webdriver.common.by import By

class TensorBannerLocators:
    BANNER = (By.CSS_SELECTOR, "div.sbisru-Contacts__border-left > a:nth-child(1)")
    REGION = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
    PARTNERS_BLOCK = (By.CLASS_NAME, "sbisru-Contacts-List__city")
    REGION_41 = (By.XPATH, "//span[contains(text(),'Камчатский край')]")
    TITLE_NAME = (By.CSS_SELECTOR, "head > title")