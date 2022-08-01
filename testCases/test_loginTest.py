import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


# To run with Pytest runner from CLI:
# Run default browser -> pytest -v -s <path-to-test-file.py>
# Run with specific browser -> pytest -v -s <path-to-test-file.py> --browser <browser-name>
# Run in parallel mode -> pytest -v -s -n=<parallel-runs-number> <path-to-test-file.py> --browser <browser-name>
# Run generating report -> pytest -v -s --html=<path-to-generate-report> <path-to-test-file.py> --browser <browser-name>
# Run with markers -> pytest -v -s -m "regression" --html=./Reports/report.html testCases/ --browser <browser-name>
class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*********** test_homePageTitle *********** ")
        self.logger.info("*********** Verifying Home Page Title *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********** Home Page title test passed *********** ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********** Home Page title test failed *********** ")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*********** Verifying Login Test *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*********** Login Test passed *********** ")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("*********** Login Test failed *********** ")
            assert False
