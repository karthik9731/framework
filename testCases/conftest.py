import configparser
from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("detach",True)
        driver = webdriver.Chrome(options=opt)
        print("launching a chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")