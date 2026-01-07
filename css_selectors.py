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
driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions')

# 'Create Account' button
$$("h1.flex--item.fs-headline1")

# paragraph under 'Create Account' button
$$("div.flex--item.js-terms.fs-caption.fc-black-400.ta-left")

# for email text box
$$("input#email")

# for password text box
$$("input#password")

# reveal pw
$$("svg.ps-absolute[aria-hidden='true']")

# 'Sign Up' button
$$("button#submit-button[name='submit-button']")

# sign up with Google
$$("button[data-provider='google']")

# sign up with Github
$$("button[data-provider='github']")

# free stackoverflow for 50 years
$$("div.fs-body1.fc-black-400")

