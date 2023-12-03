from selenium.webdriver.common.by import By


class MyAccountLocators:
    my_account_tab = (By.XPATH, "//li[@id='menu-item-22']/a[@class='nav__link']")
    login_error_list = (By.XPATH, "//ul[@class='woocommerce-error']/li")
    login_email = (By.XPATH, "//input[@name='username']")
    login_password = (By.XPATH, "//input[@name='password']")
    sign_in_button = (By.NAME, "Login")
    log_out_button = (By.XPATH, "//a[contains(text(), 'Logout')]")
    registration_email = (By.XPATH, "//input[@type='email']")
    registration_password = (By.XPATH, "//input[@autocomplete='new-password']")
    registration_button = (By.NAME, "register")
    registration_error_list = (By.XPATH, "//ul[@role='alert']/li")
    registration_data_link = "C:\\Users\\kamil\\PycharmProjects\\Selenium_Python_DDT\\Data\\registration.csv"

class AddressLocators:
    address_tab = (By.XPATH, "//a[contains(text(), 'Addresses')]")
    address_edit_tab = (By.XPATH, "//a[contains(text(), '//header/h3[contains(text(), 'Shipping address')]/following-sibling::*')]")

class AddressEditLocators:
    address_country_combo = (By.XPATH, "//input[@role='combobox']")
    address_country = (By.XPATH, "//span[@role='combobox']")
    address_last_name = (By.XPATH, "//input[@id='shipping_last_name']")
    address_name = (By.XPATH, "//input[@id='shipping_first_name']")
    address_street = (By.XPATH, "//input[@name='shipping_address_1']")
    address_zip_code = (By.XPATH, "//input[@id='shipping_postcode']")
    address_town = (By.XPATH, "//input[@id='shipping_city']")
    address_save_button = (By.XPATH, "//button[@name='save_address']")
    address_changed_message = (By.XPATH, "//div[@class='woocommerce-message'")
    address_country_index = (By.XPATH, "//li[@tabindex='-1']")

class ShopLocators:
    shop_button = (By.XPATH, "//li[@id='menu-item-21']/a[@class='nav__link']")
    shop_product = (By.XPATH, "//h2[@class='woocommerce-loop-product__title']")