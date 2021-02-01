from selenium.webdriver.support.ui import WebDriverWait as wait
import steps.common_steps
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
from selenium.common.exceptions import NoSuchElementException  



def click(context, element):
        try:
            wait(context.driver, 10).until(expected_conditions.visibility_of_element_located(element)).click()
        except:
            print(f'Cant click {element}')


def type_in(context, element, text):
        try:
            wait(context.driver, 10).until(expected_conditions.visibility_of_element_located(element)).send_keys(text)
        except:
            print(f'Error with typing in {element}')


def get_url(context):
        time.sleep(3)
        url = context.driver.current_url
        return url


def check_exists_by_xpath(context, xpath):
    try:
        context.driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True