import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from time import sleep

class Test_002_DDt_Login:
    baseUrl = ReadConfig.getApplicationURL()
    path = r"C:\Users\ckart\PycharmProjects\pythonProject1\fg_project\TestData\LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        print("Number of rows in a excel:",self.rows)

        for r in range(2,self.rows+1):   # start_index,end_index+1,step_value
            self.user = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtils.readData(self.path,"Sheet1",r,3)

            lst_status = []
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.ClickLogin()
            sleep(2)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*******PASSED*******")
                    self.lp.ClickLogout();
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*******FAILED********")
                    self.lp.ClickLogin();
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****FAILED******")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("********PASSED*******")
                    lst_status.append("Pass")

        if 'fail' not in lst_status:
            self.logger.info("LOGIN DDT TEST PASSED")
            self.driver.close()
            assert True
        else:
            self.logger.info("LOGIN DDT TEST FAILED")
            self.driver.close()
            assert False

        self.logger.info("****************END OF LOGIN DDT TEST****************")
        self.logger.info("****************completed TC_login_ddt_002 test************")






