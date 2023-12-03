import pytest
import allure
from Pages.my_account_po import MyAccountPO
from Pages.addresses_po import AddressPO
from Pages.addresses_edit_po import AddressEditPO
from OwnLibs.CSVReader import read_csv
from Data.Variables import AllVars


@pytest.mark.usefixtures("setup")
class TestAddress:

    @allure.title("S_1005, TC_1013")
    @allure.description("User should be able to change shipping address when logged in")
    def test_address_edit(self, setup):
        self.driver.get(AllVars.home_url)
        address = AddressPO(self.driver)
        address_edit = AddressEditPO(self.driver)
        my_account = MyAccountPO(self.driver)
        my_account.navigate_to()
        my_account.login_email_input(AllVars.correct_email)
        my_account.login_password_input(AllVars.correct_password)
        my_account.submit_login_form()
        my_account.verify_logged_in()
        address.navigate_to()
        address.navigate_to_address_edit()
        address_data = read_csv(AllVars.address_data_link)
        address_edit.address_input_first_name(address_data[1])
        address_edit.address_input_last_name(address_data[2])
        address_edit.address_input_country(address_data[3])
        address_edit.address_input_street(address_data[4])
        address_edit.address_input_zipcode(address_data[5])
        address_edit.address_input_town(address_data[6])
        address_edit.address_form_submit()
        address.verify_address_changed()
        my_account.log_out()