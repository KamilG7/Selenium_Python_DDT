from Locators.Locators import AddressEditLocators
from OwnLibs.Keywords import *
import logging


class AddressEditPO:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Input first name in address edit tab")
    def address_input_first_name(self, first_name):
        self.logger.info("Input first name in address edit tab")
        lib_input_text(self.driver, AddressEditLocators.address_first_name, first_name)
        allure.attach(self.driver.get_screenshot_as_png(), name="First name input",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Input last name in address edit tab")
    def address_input_last_name(self, last_name):
        self.logger.info("Input last name in address edit tab")
        lib_input_text(self.driver, AddressEditLocators.address_last_name, last_name)
        allure.attach(self.driver.get_screenshot_as_png(), name="Last name input",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Input country")
    def address_input_country(self, country):
        self.logger.info("Input country in address edit tab")
        lib_click(self.driver, AddressEditLocators.address_country)
        lib_input_text(self.driver, AddressEditLocators.address_country_combo, country)
        lib_click(self.driver, AddressEditLocators.address_country_index)
        allure.attach(self.driver.get_screenshot_as_png(), name="Country input",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Input street address")
    def address_input_street(self, street):
        self.logger.info("Input street address in address edit tab")
        lib_input_text(self.driver, AddressEditLocators.address_street, street)
        allure.attach(self.driver.get_screenshot_as_png(), name="Street input",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Input zipcode")
    def address_input_zipcode(self, zipcode):
        self.logger.info("Input zipcode in address edit tab")
        lib_input_text(self.driver, AddressEditLocators.address_zip_code, zipcode)
        allure.attach(self.driver.get_screenshot_as_png(), name="zipcode input",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Input Town")
    def address_input_town(self, town):
        self.logger.info("Input Town in address edit tab")
        lib_input_text(self.driver, AddressEditLocators.address_town, town)
        allure.attach(self.driver.get_screenshot_as_png(), name="town input",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Submit address form")
    def address_form_submit(self):
        self.logger.info("Submit address form")
        lib_click(self.driver, AddressEditLocators.address_save_button)
        allure.attach(self.driver.get_screenshot_as_png(), name="Submit address form",
                      attachment_type=AttachmentType.PNG)