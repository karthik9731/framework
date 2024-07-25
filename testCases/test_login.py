import pytest
from selenium import webdriver
from time import sleep
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homepageTitle(self,setup):
        self.logger.info("**********************Test_001_Login********************")
        self.logger.info("**********************Verifying home page title ******************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************home page title is passed******************")
        else:
            self.driver.save_screenshot(r"C:\Users\ckart\PycharmProjects\pythonProject1\fg_project\Screenshots\home_page.png")
            self.driver.close()
            self.logger.info("**************** home page failed ******************")
            assert False

    def test_login(self,setup):
        self.logger.info("*********************Verifying Login test*****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        sleep(2)
        self.lp.ClickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***************** Login test is passed *************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(r"C:\Users\ckart\PycharmProjects\pythonProject1\fg_project\Screenshots\test_logins.png")
            self.driver.close()
            self.logger.info("********************* Login test is failed ********************")
            assert False


