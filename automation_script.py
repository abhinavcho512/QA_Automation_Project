from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Test Case 1: Add Package
    driver.get("https://ecspro-qa.kloudship.com")
    driver.find_element(By.ID, "username").send_keys("kloudship.qa.automation@mailinator.com")
    driver.find_element(By.ID, "password").send_keys("Password1", Keys.RETURN)

    time.sleep(3)  # Wait for page load
    driver.find_element(By.LINK_TEXT, "Package Types").click()

    driver.find_element(By.ID, "add-manually-btn").click()

    first_name, last_name = "FirstName", "LastName"
    driver.find_element(By.ID, "package-name").send_keys(f"{first_name}_{last_name}")
    driver.find_element(By.ID, "package-dimensions").send_keys(str(random.randint(1, 20)))
    driver.find_element(By.ID, "save-package-btn").click()

    # Test Case 2: Delete Package
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Package Types").click()

    package_to_delete = f"{first_name}_{last_name}"
    driver.find_element(By.XPATH, f"//tr[td[text()='{package_to_delete}']]/td/button[text()='Delete']").click()

    # Logout
    driver.find_element(By.ID, "logout-btn").click()

finally:
    driver.quit()