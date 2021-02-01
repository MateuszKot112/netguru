from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver



def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.implicitly_wait(3)
    



def after_scenario(context, scenario):
    context.driver.quit()