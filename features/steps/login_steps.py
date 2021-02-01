from selenium.webdriver.common.by import By
import steps.common_steps as do
import time


EMAIL                 = (By.NAME, 'email')
PASSWORD              = (By.NAME, 'password')
SIGN_IN_BUTTON        = (By.XPATH, "//div[@class='login-component']//button[1]")
INAVLID_EMAIL_ALERT   = ("//mat-error[@id='mat-error-2']")
ERROR_PASSWORD        = ("//span[contains(text(),'Email or password not valid')]")


@when('I provide valid email "{email}" and "{password}"')
def step_impl(context, email, password):
    do.type_in(context, EMAIL, email)
    do.type_in(context, PASSWORD, password)

@when('I provide invalid "{email}" and "{password}"')
def step_impl(context, email, password):
    do.type_in(context, EMAIL, email)
    do.type_in(context, PASSWORD, password)

@when('I click on Sign In button')
def click_sigin_button(context):
    do.click(context, SIGN_IN_BUTTON)


@then('Home page is present')
def step_impl(context):
    #sleep is needed for url change
    time.sleep(3)
    assert 'home' in do.get_url(context), 'Home Page'

@then("Error message should appear")
def error_message_present(context):
    check_invalid_password = do.check_exists_by_xpath(context, ERROR_PASSWORD )
    check_invalid_email = do.check_exists_by_xpath(context, INAVLID_EMAIL_ALERT )
    if check_invalid_email or check_invalid_password:
        assert True
    else:
        assert False

