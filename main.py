from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path ="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.co.uk/")

#find the element we want to interact with and add the interaction
input_element = driver.find_element(By.ID, "twotabsearchtextbox")
input_element.send_keys("Woman dresses" + Keys.ENTER)

# Wait for the intercepting form and accept it
try:
    form = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "sp-cc")))
    accept_button = form.find_element(By.XPATH, "//input[@type='submit']")
    accept_button.click()
except Exception as e:
    print("No intercepting form found or error in handling it:", e)

# After waiting click on the link
link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "summer casual")))
link.click()

time.sleep(20)
driver.quit()