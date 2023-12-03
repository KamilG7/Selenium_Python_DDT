import pytest
import allure
from Pages.my_account_po import MyAccountPO
from Data.Variables import AllVars
from Pages.shop_po import ShopPO


@pytest.mark.usefixtures("setup")
class TestShop:

    @allure.title("S_100, TC_1014")
    @allure.description("User should have access to products in shop tab")
    def test_correct_login(self, setup):
        self.driver.get(AllVars.home_url)
        my_account = MyAccountPO(self.driver)
        my_account.navigate_to()
        my_account.login_email_input(AllVars.correct_email)
        my_account.login_password_input(AllVars.correct_password)
        my_account.submit_login_form()
        my_account.verify_logged_in()
        shop = ShopPO(self.driver)
        shop.navigate_to()
        shop.check_if_products_displayed()
