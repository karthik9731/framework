from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# driver = webdriver.Chrome()

class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[text()='Log in']"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver = driver  # instance variable

    def setUsername(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        sleep(2)
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        sleep(2)
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def ClickLogout(self):
       self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()