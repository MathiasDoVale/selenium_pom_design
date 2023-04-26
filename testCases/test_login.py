import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):

        self.logger.info("**************** Test_001_Login ****************")
        self.logger.info("**************** Verifying Home Page Title ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************** Home Page title test is passed ****************")
        else:
            self.driver.save_screenshot("\\.screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**************** Home Page title test failed ****************")
            assert False
    
    def test_login(self, setup):
        self.logger.info("**************** Verifying Login Test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**************** Login Test is passed ****************")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("**************** Login Test failed ****************")
            assert False