from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# click top Amazon image
driver.find_element(By.XPATH, "//a[@class='a-link-nav-icon']").click()
#sleep(1)
driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()

# input email for login
email_input = driver.find_element(By.ID, 'ap_email_login')
email_input.clear()
email='silasaction@gmail.co'
email_input.send_keys(email)
#sleep(3)

# click continue button
driver.find_element(By.XPATH,"//input[@class='a-button-input']").click()

# go back to login page
driver.find_element(By.XPATH,"//a[@class='a-link-normal change-claim']").click()
#sleep(2)

# conditions of use
driver.find_element(By.LINK_TEXT,"Conditions of Use").click()

# privacy notice
driver.find_element(By.LINK_TEXT,"Privacy Notice").click()
sleep(2)
driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()

# 'need help' link
driver.find_element(By.LINK_TEXT,"Need help?").click()
#sleep(2)

# forgot password
# the following links were not present on the site at this time
#driver.select_element(By.LINK_TEXT,"Forgot your password?").click()
#driver.find_element(By.LINK_TEXT, 'Other issues with sign-in').click()

# create an account
driver.find_element(By.LINK_TEXT,"Create a free business account").click()

# tests completed successfully
print('Test Passed!!!')
driver.quit()

#target results
driver.find_element(By.XPATH,"//div[contains(@class,'styles_listingPageResultsCount')]").text