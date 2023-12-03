import pytest
import allure
import OwnLibs.CSVReader
from Pages.my_account_po import MyAccountPO
from Data.Variables import AllVars



@pytest.mark.usefixtures("setup")
class TestLogin:

    @allure.title("S_1003, TC_1006")
    @allure.description("Login should succeed with valid credentials")
    def test_correct_login(self, setup):
        self.driver.get(AllVars.home_url)
        my_account = MyAccountPO(self.driver)
        my_account.navigate_to()
        my_account.login_email_input(AllVars.correct_email)
        my_account.login_password_input(AllVars.correct_password)
        my_account.submit_login_form()
        my_account.verify_logged_in()
        my_account.log_out()

    @allure.title("S_1004, TC_1007, TC_1008, TC_1009, TC_1010, TC_1011, TC_1012")
    @allure.description("Login with invalid data should display correct error messages")
    def test_incorrect_login(self, setup):
        for login_credentials in OwnLibs.CSVReader.read_csv(AllVars.login_data_link):
            self.driver.get(AllVars.home_url)
            my_account = MyAccountPO(self.driver)
            my_account.navigate_to()
            my_account.login_email_input(login_credentials[0])
            my_account.login_password_input(login_credentials[1])
            my_account.submit_login_form()
            my_account.verify_registration_error(login_credentials[2])