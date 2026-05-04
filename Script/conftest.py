import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config import BROWSER, HEADLESS, GECKODRIVER_PATH, LOGIN_URL, MAIN_URL, CREATE_URL
from tool import Logger
from Page.login_page import LoginPage
from Page.main_page import MainPage
from Page.create_page import CreatePage
        


@pytest.fixture(scope='session')
def logger():
    """日志 fixture,整个测试会话共用一个 logger 实例"""
    return Logger()


@pytest.fixture(scope='function')
def driver(logger):
    logger.info(f'===== 启动浏览器: {BROWSER} =====')

    if BROWSER.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        if HEADLESS:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    elif BROWSER.lower() == 'edge':
        options = webdriver.EdgeOptions()
        if HEADLESS:
            options.add_argument('--headless')
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )
    elif BROWSER.lower() == 'firefox':
        options = webdriver.FirefoxOptions()
        if HEADLESS:
            options.add_argument('--headless')
        driver = webdriver.Firefox(
            service=FirefoxService(executable_path=GECKODRIVER_PATH),
            options=options
        )
    else:
        raise ValueError(f'不支持的浏览器类型: {BROWSER}')

    # driver.maximize_window()
    # 全屏
    driver.fullscreen_window()

    yield driver

    logger.info('===== 关闭浏览器 =====')
    driver.quit()


@pytest.fixture(scope='function')
def login_page(driver, logger):
    """LoginPage 页面对象 fixture - 自动打开登录页"""
    driver.get(LOGIN_URL)
    logger.info(f'打开测试地址: {LOGIN_URL}')
    return LoginPage(driver)

@pytest.fixture(scope='function')
def main_page(driver, logger):
    """MainPage 页面对象 fixture - 自动打开主页"""
    driver.get(MAIN_URL)
    logger.info(f'打开测试地址: {MAIN_URL}')
    return MainPage(driver)

@pytest.fixture(scope='function')
def create_page(driver, logger):
    """CreatePage 页面对象 fixture - 自动打开添加页"""
    driver.get(CREATE_URL)
    logger.info(f'打开测试地址: {CREATE_URL}')  
    return CreatePage(driver)
