import allure
import pytest
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@allure.severity(allure.severity_level.NORMAL)
class TestHRM:
    baseURL = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.baseURL)
        status = self.driver.find_element(By.XPATH, "//*[@id='divLogo']/img").is_displayed()

        if status == True:
            assert True
        else:
            assert False

        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listEmployees(self):
        pytest.skip('Skipping test... later I will implement')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.baseURL)

        self.driver.find_element(By.ID, "txtUsername").send_keys(self.username)
        self.driver.find_element(By.ID, "txtPassword").send_keys(self.password)
        self.driver.find_element(By.ID, "btnLogin").click()

        act_title = self.driver.title
        if act_title == "OrangeHRM123":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
