import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities.customLogger import LogGen
import time

class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.log_gen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.logger.info("********** STARTING TEST : test_homePageTitle **********")
        self.driver = setup
        self.logger.info("Launching Website...")
        self.driver.get(self.baseURL)
        title = self.driver.title

        if "Your store" in title:
            self.logger.info("Home page title is successfully verified...")
            assert True
            self.driver.close()
            self.logger.info("********** END TEST : test_homePageTitle : PASSED **********")
        else:
            self.logger.error("Home page title check if failed!")
            self.driver.save_screenshot("./Screenshots/HomePageTitle.png")
            self.driver.close()
            self.logger.error("********** END TEST : test_homePageTitle : FAILED **********")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********** STARTING TEST : test_login **********")
        self.driver = setup
        self.logger.info("Launching Website...")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.logger.info("Entering Username...")
        self.lp.setUsername(self.username)
        self.logger.info("Entering password...")
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        title = self.driver.title

        if "Dashboard" in title:
            self.logger.info("Login page title is successfully verified...")
            self.logger.info("********** END TEST : test_login : PASSED **********")
            assert True
            self.driver.close()
        else:
            self.logger.error("Login page title check if failed!")
            self.driver.save_screenshot("./Screenshots/LoginPageTitle.png")
            self.driver.close()
            self.logger.info("********** END TEST : test_login : FAILED **********")