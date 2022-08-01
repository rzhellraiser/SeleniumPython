import time
import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("*********** Test_005_SearchCustomerByName *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********** Login successful *********")

        self.logger.info("*********** Starting Search Customer By Name *********")

        self.addcust = AddCustomer(self.driver)
        time.sleep(3)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("*********** Searching Customer By Name *********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()

        time.sleep(5)

        status = searchcust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("************ Test_005_SearchCustomerByName Finished *************")
        self.driver.close()
