#
# Need to assign an answer first
#
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import time

options = Options()
options.add_argument("--headless")


driver = webdriver.Chrome(chrome_options=options)
driver.get('https://gremlins-api.reddit.com/room?nightmode=1')

print("Enter Reddit Username")
usr = input()

print("Enter Reddit Password")
password = input()

# Log in user
driver.find_element_by_id("loginUsername").send_keys(usr)
driver.find_element_by_id("loginPassword").send_keys(password)
time.sleep(2)
driver.find_element_by_class_name("AnimatedForm__submitButton").click()
time.sleep(10)
print("Logged in!")

try:
    while True:
        res = driver.find_elements_by_xpath("//gremlin-note")
        random.choice(res).click()
        time.sleep(6)
        driver.find_elements_by_xpath("//gremlin-action")[0].click()
        time.sleep(5)

except KeyboardInterrupt:
    print("Exiting please wait...")
    driver.quit()