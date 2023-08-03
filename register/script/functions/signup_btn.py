import json
import json
from selenium.webdriver.common.by import By

elements_path ='register/paths/signup_elements.json'
signup_data_path = 'register/data/signup_data.json'

def func_signup_btn_v1(self):
    # Read data from the JSON file
    with open(signup_data_path) as json_file:
        data = json.load(json_file)
        entry_name = data[0]['name']
        entry_email = data[0]['email']

    # Read XPath data from the JSON file
    with open('../data/sign_up_xpath.json') as xpath_file:
        xpath_data = json.load(xpath_file)

    xpath_name = None
    xpath_email = None
    xpath_sign_up_btn = None
    for field_data in xpath_data:
        field_name = field_data['field_name']
        if field_name == 'name':
            xpath_name = field_data['xpath']
        elif field_name == 'email':
            xpath_email = field_data['xpath']
        elif field_name == 'sign_up_btn':
            xpath_sign_up_btn = field_data['xpath']

    # Fill up the form using the obtained XPaths and data
    # Enter a Name
    if xpath_name:
        element_name = self.driver.find_element(By.XPATH, xpath_name)
        element_name.send_keys(entry_name)

    # Enter a Email
    if xpath_email:
        element_email = self.driver.find_element(By.XPATH, xpath_email)
        element_email.send_keys(entry_email)

    # Click on sign_up button
    if xpath_sign_up_btn:
        element_btn = self.driver.find_element(By.XPATH, xpath_sign_up_btn)
        element_btn.click()


def func_signup_btn_v2(self):
    # Read data from the JSON file
    with open(signup_data_path) as json_file:
        data = json.load(json_file)[0]  # Load only the first set of data

    # Read XPath data from the JSON file
    with open(elements_path) as xpath_file:
        xpath_data = json.load(xpath_file)

    # Create a dictionary to map field names to XPaths
    xpath_dict = {}
    for field_data in xpath_data:
        field_name = field_data['field_name']
        xpath_dict[field_name] = field_data['xpath']

    # Fill up the form using the obtained XPaths and data
    for field_name, xpath in xpath_dict.items():
        if field_name in data:
            element = self.driver.find_element(By.XPATH, xpath)
            field_value = data[field_name]
            element.send_keys(field_value)

    # Click on the sign-up button
    if 'sign_up_btn' in xpath_dict:
        sign_up_btn_xpath = xpath_dict['sign_up_btn']
        sign_up_btn = self.driver.find_element(By.XPATH, sign_up_btn_xpath)
        sign_up_btn.click()