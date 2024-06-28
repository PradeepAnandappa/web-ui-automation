from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from Configuration.config import config


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="my option: chrome or firefox",
        choices=("chrome", "firefox", "grid")
    )
    parser.addoption(
        "--env",
        action="store",
        default="production",
        help="my option: staging or production",
        choices=("staging", "production")
    )


@pytest.fixture
def getEnvironment(request):
    return request.config.getoption("--env", default="production")


@pytest.fixture
def getBrowser(request):
    return request.config.getoption("--browser", default="chrome")


@pytest.fixture
def setup_driver(request, getBrowser, getEnvironment):
    if getBrowser == "chrome":
       #web_driver = webdriver.Chrome(executable_path=config.chromeDriver)
        chromeOptions = webdriver.ChromeOptions()
        file_path = str(Path.home()) + "\\PycharmProjects\\allgeo_web_app_pro\\src\\Resources\\Download"
        print("download directory: "+file_path)

        chromeOptions.add_argument("--window-size=1920,1080")
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--proxy-server='direct://'")
        chromeOptions.add_argument("--proxy-bypass-list=*")
        chromeOptions.add_argument("--start-maximized")
        #chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--disable-gpu')
        chromeOptions.add_argument('--disable-dev-shm-usage')
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--ignore-certificate-errors')
        prefs = {"download.default_directory": file_path, "profile.default_content_setting_values.automatic_downloads": 1}
        chromeOptions.add_experimental_option("prefs", prefs)
        web_driver = webdriver.Chrome(options=chromeOptions)
    elif getBrowser == "firefox":
        web_driver = webdriver.Firefox(executable_path=config.firefoxDriver)

    elif getBrowser == "grid":
        hub_url = "http://localhost:4444/wd/hub"
        desired_capabilities = DesiredCapabilities.CHROME  # Change this to your desired browser
        web_driver = webdriver.Remote(hub_url, desired_capabilities=desired_capabilities)

    if getEnvironment == "staging":
        config.baseURL = config.stageURL
        #web_driver.get(config.stageURL)
    elif getEnvironment == "production":
        config.baseURL = config.prodURL
         #web_driver.get(config.prodURL)
    web_driver.get(config.baseURL)
    web_driver.fullscreen_window()

    web_driver.implicitly_wait(2)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    web_driver.quit()
