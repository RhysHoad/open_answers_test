import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def open_test():

    # setup 
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(chrome_options=options)
    URL = 'https://www.openanswers.co.uk/careers/join-us'
    wait = WebDriverWait(driver, 10)

    driver.get(URL)
    try:
        ## GET THE SUM
        sum = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "question"))
        )
    finally:
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
        return(r_message_text)
    else:
        return("Oops, something went wrong")

    # teardown
    driver.close()

open_test()