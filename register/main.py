
import unittest
from selenium import webdriver

from script.functions.signup_btn import func_signup_btn_v2, func_signup_btn_v1
from script.functions.create_btn import func_create_btn_v1

# Login Site
login_site = "https://www.automationexercise.com/login"
logged_site = "https://www.automationexercise.com/"

class SignupTestPositive(unittest.TestCase):

    def setUp(self):
        # Set up the webdriver for your preferred browser (e.g., Chrome)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        
    # Validate Signup Button with non-existing email
    def test_signup_button(self):
        # Navigate to the signup page
        self.driver.get(login_site)
        func_signup_btn_v1(self)

    def tearDown(self):
        # Close the browser after completing the signup process
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()