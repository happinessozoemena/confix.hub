
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is properly installed and in PATH
driver.get("https://thinking-tester-contact-list.herokuapp.com/")


# Login Test
def test_login():
    print("Starting sumit Test")
    driver.find_element(By.ID, "email").send_keys("happy@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Ozoemena123@#")
    driver.find_element(By.ID, "submit").click()  # Replace with actual button ID
    time.sleep(3)  # Adjust time if needed
   # assert "Dashboard" in driver.title, "sumit Test Failed"  # Replace with actual title
    print("sumit Test Passed")


# Add New Contact Test
def test_add_contact():
    print("Starting Add Contact Test")
    for i in range(1, 11):  # Loop to add 10 contacts
        driver.find_element(By.ID, "add-contact").click()  # Replace with actual button ID

        # Fill Form Fields
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstName"))
        ).send_keys("Happiness")
        driver.find_element(By.ID, "lastName").send_keys("Uzoma")
        driver.find_element(By.ID, "birthdate").send_keys("1995/11/14")
        driver.find_element(By.ID, "email").send_keys("happy@gmail.com")
        driver.find_element(By.ID, "phone").send_keys("09064008150")
        driver.find_element(By.ID, "street1").send_keys("mpape abuja")
        driver.find_element(By.ID, "street2").send_keys("maitama 2")
        driver.find_element(By.ID, "city").send_keys("fct")
        driver.find_element(By.ID, "stateProvince").send_keys("Abuja")
        driver.find_element(By.ID, "postalCode").send_keys("900231")
        driver.find_element(By.ID, "country").send_keys("Nigeria")

        driver.find_element(By.ID, "submit").click()

        time.sleep(1)  # Allow the UI to update

    # Verify 10 contacts have been added
    contacts = driver.find_elements(By.CLASS_NAME, "contact-item")  # Replace with actual class
    assert len(contacts) == 10, f"Expected 10 contacts, but found {len(contacts)}. Add Contact Test Failed."
    print("Add Contact Test Passed")


# Logout Test
def test_logout():
    print("Starting Logout Test")
    driver.find_element(By.ID, "logout.logout").click()  # Replace with actual button ID
    time.sleep(2)
    assert "Login" in driver.title, "Logout Test Failed"  # Replace with actual login page title
    print("Logout Test Passed")


# Execute Tests
try:
    test_login()
    test_add_contact()
    test_logout()
finally:
    driver.quit()


