from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

from selenium.webdriver.common.by import By

import string
import random
import pytest


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********* Test_003_AddCustomer *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login successful *********")

        self.logger.info("********* Starting Add Customer Test *********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("********* Providing Customer Info *********")

        self.email = self.random_generator(8) + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Renzo")
        self.addcust.setLastName("Castaneda")
        self.addcust.setDob("6/26/1990")  # Format D/MM/YYYY
        self.addcust.setCompanyName("MasterRz")
        self.addcust.setAdminComment("This is for testing ....")
        self.addcust.clickOnSave()

        self.logger.info("********* Saving Customer Info *********")

        self.logger.info("********* Add customer validation started *********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_src.png")  # Screenshot
            self.logger.error("****** Add Customer Test Failed ********")
            assert True == False

        self.driver.close()
        self.logger.info("******* Ending Add Customer Test *******")

    def random_generator(char_num):
        return ''.join(random.choice(string.ascii_letters) for x in range(char_num))
