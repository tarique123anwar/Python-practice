import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTestCase:
    def setUp(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # URL of the login page
        self.login_url = "https://test.admin.experiense.ai/"
        self.wait = WebDriverWait(self.driver, 10)

    def test_successful_login(self):
        # Navigate to the login page
        self.driver.get(self.login_url)
        # Find the username and password input fields and submit button
        username_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#email-login")))
        password_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password-login")))
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        # Enter the username and password
        username_field.send_keys("superadmin")
        password_field.send_keys("Experiense@123")
        # Click on the login button
        login_button.click()
        # Check if login was successful by verifying the presence of a welcome message
        welcome_message = self.wait.until(EC.visibility_of_element_located((By.ID, "welcome-message")))
        self.assertTrue(welcome_message.is_displayed())

    def test_invalid_login(self):
        # Navigate to the login page
        self.driver.get(self.login_url)
        # Find the username and password input fields and submit button
        username_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#email-login")))
        password_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password-login")))
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        # Enter invalid username and password
        username_field.send_keys("invalid_user")
        password_field.send_keys("invalid_password")
        # Click on the login button
        login_button.click()
        # Check if error message is displayed
        error_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='alert']")))
        self.assertTrue(error_message.is_displayed())

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
