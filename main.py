import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
response = requests.get("https://courses.upenn.edu/")
print(response.status_code)
'''

driver = webdriver.Firefox()
driver.get("http://courses.upenn.edu/")

#store main courses page
main_page = driver.current_window_handle
assert "Search" in driver.title


#locates the login button in the top right corner
login_button = driver.find_element(By.CSS_SELECTOR, ".fa.fa-sign-in")
login_button.click()

WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
print(driver.window_handles)
for window_handle in driver.window_handles:
    if window_handle != main_page:
        driver.switch_to.window(window_handle)
        break

#at this point we are in the second pop-up window where you put in your login info
#project is currently on hold as I figure out how to (if it's possible) to work around 2FA, phone code


while True:
    continue
driver.close()

