import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from Locators.Locators import MyAccountLocators
from OwnLibs.Keywords import *


class MyAccountPO:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Navigate To My Account")
    def navigate_to(self):
        self.logger.info("Navigating to My Account Page")
        lib_click(self.driver, MyAccountLocators.my_account_tab)
        allure.attach(self.driver.get_screenshot_as_png(), name="Navigating to My Account Page",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Input email to registration form")
    def registration_email_input(self, email):
        self.logger.info("Input user email to registration form")
        if email == "#BLANK":
            pass
        else:
            lib_input_text(self.driver, MyAccountLocators.registration_email, email)
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Input email to registration form", attachment_type=AttachmentType.PNG)

    @allure.step("Input password to registration form")
    def registration_password_input(self, password):
        self.logger.info("Input password to registration form")
        if password == "#BLANK":
            pass
        else:
            lib_input_text(self.driver, MyAccountLocators.registration_password, password)
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Input password to registration form", attachment_type=AttachmentType.PNG)

    @allure.step("Submit Registration Form")
    def submit_registration_form(self):
        self.logger.info("Submit Registration Form")
        lib_click(self.driver, MyAccountLocators.registration_button)
        allure.attach(self.driver.get_screenshot_as_png(), name="Submit Registration Form",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Verify logged in successfully")
    def verify_logged_in(self):
        self.logger.info("Verify logged in successfully")
        lib_is_displayed(self.driver, MyAccountLocators.log_out_button)
        allure.attach(self.driver.get_screenshot_as_png(), name="Verify logged in successfully",
                      attachment_type=AttachmentType.PNG)

    @allure.step("User logs out")
    def log_out(self):
        self.logger.info("User logs out")
        lib_click(self.driver, MyAccountLocators.log_out_button)
        allure.attach(self.driver.get_screenshot_as_png(), name="Log out", attachment_type=AttachmentType.PNG)

    @allure.step("Verify if error associated with data is correct")
    def verify_registration_error(self, error):
        self.logger.info("Verify if error associated with data is correct")
        assert error in lib_get_text(self.driver, MyAccountLocators.registration_error_list)
        allure.attach(self.driver.get_screenshot_as_png(), name="Verify error", attachment_type=AttachmentType.PNG)

    @allure.step("Input email to login form")
    def login_email_input(self, email):
        self.logger.info("Input email to login form")
        if email == "#BLANK":
            pass
        else:
            lib_input_text(self.driver, MyAccountLocators.login_email, email)
            allure.attach(self.driver.get_screenshot_as_png(), name="Input email to login form",
                          attachment_type=AttachmentType.PNG)

    @allure.step("Input password to registration form")
    def login_password_input(self, password):
        self.logger.info("Input password to login form")
        if password == "#BLANK":
            pass
        else:
            lib_input_text(self.driver, MyAccountLocators.login_password, password)
            allure.attach(self.driver.get_screenshot_as_png(), name="Input password to login form",
                          attachment_type=AttachmentType.PNG)

    @allure.step("Submit Login Form")
    def submit_login_form(self):
        self.logger.info("Submit Login Form")
        lib_click(self.driver, MyAccountLocators.sign_in_button)
        allure.attach(self.driver.get_screenshot_as_png(), name="Submit Login Form",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Verify if error associated with data is correct")
    def verify_login_error(self, error):
        self.logger.info("Verify if error associated with data is correct")
        assert error in lib_get_text(self.driver, MyAccountLocators.login_error_list)
        allure.attach(self.driver.get_screenshot_as_png(), name="Verify error", attachment_type=AttachmentType.PNG)