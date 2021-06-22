from selenium import webdriver
import pytest
from utilities.customLogger import LogGen


@pytest.fixture()
def setup(browser):
    logger = LogGen.log_gen()
    if browser == 'chrome':
        logger.info("Launching chrome browser... ")
        driver = webdriver.Chrome(executable_path='/Users/maneeshkumar/Documents/workspace/drivers/chromedriver')
        driver.maximize_window()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        logger.info("Launching firefox browser... ")
        driver = webdriver.Firefox(executable_path='/Users/maneeshkumar/Documents/workspace/drivers/geckodriver')
        driver.maximize_window()
        print("Launching firefox browser.........")
    elif browser == 'edge':
        logger.info("Launching EDGE browser... ")
        driver = webdriver.Ie(executable_path='/Users/maneeshkumar/Documents/workspace/drivers/msedgedriver')
        driver.maximize_window()
        print("Launching EDGE browser.........")
    elif browser == 'ie':
        logger.info("Launching IE browser... ")
        driver = webdriver.Ie(executable_path='/Users/maneeshkumar/Documents/workspace/drivers/IEDriverServer.exe')
        driver.maximize_window()
        print("Launching IE browser.........")
    elif browser == 'safari':
        logger.info("Launching safari browser... ")
        driver = webdriver.Safari()
        driver.maximize_window()
        print("Launching safari browser.........")
    else:
        logger.info("Launching safari browser... ")
        driver = webdriver.Safari()
        driver.maximize_window()
    return driver


# This will get the value from CLI /hooks
def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Selenium-Python Hybrid Framework'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Mk'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)