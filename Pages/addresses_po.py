from Locators.Locators import AddressLocators
from OwnLibs.Keywords import *
import logging


class AddressPO:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Navigate To Address tab")
    def navigate_to(self):
        self.logger.info("Navigating to Address tab")
        lib_click(self.driver, AddressLocators.address_tab)
        allure.attach(self.driver.get_screenshot_as_png(), name="Navigating to Address tab",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Verify Address changed")
    def verify_address_changed(self):
        self.logger.info("Verify Address changed")
        assert "Address changed successfully" in AddressLocators.address_changed_message()
        allure.attach(self.driver.get_screenshot_as_png(), name="Verify Address changed",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Navigate to address edit page")
    def navigate_to_address_edit(self):
        self.logger.info("Navigate to address edit page")
        lib_click(self.driver, AddressLocators.address_edit_tab)
        allure.attach(self.driver.get_screenshot_as_png(), name="Navigate to address edit page",
                      attachment_type=AttachmentType.PNG)