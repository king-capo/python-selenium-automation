from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# click "account"
driver.find_element(By.ID,"account-sign-in").click()
sleep(2)
# click to "sign in/create account"
# driver.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button' and @data-test='accountNav-signIn']")), message='Sign in button not clickable').click()
driver.find_element(By.XPATH,"//button[@type='button' and @data-test='accountNav-signIn']").click()

# return to homepage to search for tea
driver.get('https://www.target.com/')

search = driver.find_element(By.ID,"search")
search.clear()
search.send_keys('tea')

# verify that our 'search' worked
expected_text = '# results for "tea"'
sleep(3)
actual_text = driver.find_element(By.XPATH,"//h2[contains(@class,'styles_ndsHeading__phw6r')]").text
print(actual_text)
print(actual_text)
driver.quit()