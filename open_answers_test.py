from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

# setup 
driver = webdriver.Chrome()
URL = 'https://www.openanswers.co.uk/careers/join-us'
wait = WebDriverWait(driver, 10)
timeout = 1

try:
    driver.get(URL)
    sum = wait.until(EC.visibility_of_element_located((By.ID, 'question')))
except TimeoutException:
    print("Timed out waiting for page to load")

## GET THE SUM
sum = driver.find_element_by_id('question')
equation = (sum.text)
print(equation)

## CALCULATE THE ANSWER
solution = eval(equation)
print(eval(equation))

## PASTE THE RESULT IN THE BOX & SUBMIT
text_input = driver.find_element_by_id('ans')
text_input.send_keys(solution)
button = driver.find_element_by_id('submit')

try:
    button.click()
except TimeoutException:
    # If the loading took too long, print message and try again
    print("Loading took too much time!")

#CAPTURE THE RESPONSE & VALIDATE
r_message = wait.until(EC.visibility_of_element_located((By.ID, 'msg')))
r_message_text = r_message.text
print(r_message_text)

if "Well done" in r_message_text:
    print("Success!")
else:
    print("Oops, something went wrong")

# teardown
driver.close()