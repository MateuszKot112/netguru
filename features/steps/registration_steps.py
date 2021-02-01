from behave import then, when, given, step
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import steps.common_steps as do
import time
import random


CREATE_ACOCUNT_BUTTON      = (By.XPATH, "//body//button[2]")
NAME                       = (By.ID, "mat-input-2")
SURNAME                    = (By.ID, "mat-input-3")
CREATE_EMAIL               = (By.ID, "mat-input-4")
CREATE_PASSWORD            = (By.ID, "mat-input-5")
CONFIRM_PASSWORD           = (By.ID, "mat-input-6")
CONTINUE_BUTTON            = (By.XPATH, "//button[@class='custom-button full-btn mat-raised-button mat-button-base mat-primary']")
CUSTOMER_TYPE_DROPDOWN     = (By.XPATH, "//div[@class='mat-select-arrow']")
INDIVIDUAL_CUSTOMER        = (By.XPATH, "//span[contains(text(),'Individual')]")
VERICATION_MAIL_INFO       = ("//body/div[@id='alldiv']/rehe-root[1]/div[1]/rehe-register[1]/div[1]/rehe-successfully-create-account[1]/div[1]/div[1]/div[1]")
TOO_SHORT_PASSWORD         = ("//mat-error[@id='mat-error-8']")
INVALID_MAIL               =("//mat-error[@id='mat-error-7']")
EMAIL_TAKEN                =("//mat-dialog-container[@id='mat-dialog-0']")


def generate_email():
    list = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'z', 'x', 's', 'r']
    email = ''
    for name in range (9):
        name = random.sample(list, 1)[0]
        email += name 
    return email + "@xyza.com"


@given('The Rehegoo page "{url}" is displayed')
def sth(context, url):
    context.driver.get(url)


@when("I click on Create Account button")
def click_registration_button(context):
    do.click(context, CREATE_ACOCUNT_BUTTON)
    

@when('I provide valid data "{name}", "{last_name}", "{password}"')
def something(context, name, last_name, password):
    do.type_in(context, NAME, name)
    do.type_in(context, SURNAME, last_name)
    do.type_in(context, CREATE_EMAIL, generate_email())
    do.type_in(context, CREATE_PASSWORD, password)
    do.type_in(context, CONFIRM_PASSWORD, password)


@when('I provide invalid data "{name}", "{last_name}", "{email}", "{password}"')
def something(context, name, last_name, email, password):
    do.type_in(context, NAME, NAME)
    do.type_in(context, SURNAME, last_name)
    do.type_in(context, CREATE_EMAIL, email)
    do.type_in(context, CREATE_PASSWORD, password)
    do.type_in(context, CONFIRM_PASSWORD, password)
  

@when('I choose customer type Individual')
def choose_type(context):
    do.click(context, CUSTOMER_TYPE_DROPDOWN)
    do.click(context, INDIVIDUAL_CUSTOMER)
    
    

@when('I click on Continue button')
def click_continue_button(context):
    do.click(context, CONTINUE_BUTTON)


@then('I should see "{string}" info')
def step_impl(context, string):
    assert do.check_exists_by_xpath(context, VERICATION_MAIL_INFO)


@then("I should see error message")
def check_error_messages(context):
    check_too_short_password =  do.check_exists_by_xpath(context, TOO_SHORT_PASSWORD)
    check_invalid_email = do.check_exists_by_xpath(context, INVALID_MAIL)
    check_if_taken = do.check_exists_by_xpath(context, EMAIL_TAKEN)
    
    if check_too_short_password or check_invalid_email or check_if_taken:
        assert True
    else:
        assert False

