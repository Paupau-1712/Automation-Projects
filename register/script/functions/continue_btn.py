import json
import json
from selenium.webdriver.common.by import By

def func_continue_btn_v1(self):
    # Read XPath data from the JSON file
    with open('../data/create_accnt_xpath.json') as xpath_file:
        xpath_data = json.load(xpath_file)

    # Create a dictionary to map field names to XPaths
    for field_data in xpath_data:
        field_name = field_data['field_name']
        xpath_data[field_name] = field_data['xpath']

    # Click on the sign-up button
    if 'cont_button' in xpath_data:
        cont_btn_xpath = xpath_data['cont_button']
        cont_btn = self.driver.find_element(By.XPATH, cont_btn_xpath)
        cont_btn.click()