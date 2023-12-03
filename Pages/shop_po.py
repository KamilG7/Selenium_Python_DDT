from OwnLibs.Keywords import *
import logging
from Locators.Locators import ShopLocators


class ShopPO:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Navigate To Shop when user logged in")
    def navigate_to(self):
        self.logger.info("Navigate To Shop when user logged in")
        lib_click(self.driver, ShopLocators.shop_button)
        allure.attach(self.driver.get_screenshot_as_png(), name="Navigating to Shop",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Check products displayed")
    def check_if_products_displayed(self):
        self.logger.info("Check if logged in user see products diplayed in shop")
        lib_is_displayed(self.driver, ShopLocators.shop_product)
        allure.attach(self.driver.get_screenshot_as_png(), name="Check products displayed",
                      attachment_type=AttachmentType.PNG)
