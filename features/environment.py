from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application
from support.logger import logger


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    # ### GOOGLE CHROME ####
    driver_path = ChromeDriverManager().install()
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    #
    # ### FIREFOX ####
    # # driver_path = GeckoDriverManager().install()
    # # service = Service(driver_path)
    # # context.driver = webdriver.Firefox(service=service)
    #
    # ### HEADLESS MODE ####
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(
        options=options,
        service=service
    )
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    ### BROWSERSTACK ###
    # bs_user = 'joshparada_PxuOyC'
    # bs_key = 'ysxNqGizy9iuEt6789Ap'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": "Windows",
    #     "osVersion": "11",
    #     'browserName': 'edge',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.quit()
