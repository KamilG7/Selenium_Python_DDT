import pytest
import allure
import OwnLibs.CSVReader
from Pages.my_account_po import MyAccountPO
from Data.Variables import AllVars



@pytest.mark.usefixtures("setup")
class TestRegistration:

    @allure.title("S_1001, TC_1001")
    @allure.description("Test registration with valid credentials")
    def test_correct_registration(self, setup):
        self.driver.get(AllVars.home_url)
        my_account = MyAccountPO(self.driver)
        my_account.navigate_to()
        my_account.registration_email_input(AllVars.correct_email)
        my_account.registration_password_input(AllVars.correct_password)
        my_account.submit_registration_form()
        my_account.verify_logged_in()
        my_account.log_out()

    @allure.title("S_1002, TC_1002, TC_1003, TC_1004, TC_1005, TC_1006")
    @allure.description("Registration with invalid data should display correct error messages")
    def test_correct_registration(self, setup):
        for registration_data in OwnLibs.CSVReader.read_csv(AllVars.registration_data_link):
            self.driver.get(AllVars.home_url)
            my_account = MyAccountPO(self.driver)
            my_account.navigate_to()
            my_account.registration_email_input(registration_data[0])
            my_account.registration_password_input(registration_data[1])
            my_account.submit_registration_form()
            my_account.verify_registration_error(registration_data[2])
