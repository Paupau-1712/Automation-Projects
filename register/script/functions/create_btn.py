import json
from selenium.webdriver.common.by import By



def func_create_btn_v1(self):
    # Read data from the JSON file
    with open('../data/signup_data.json') as json_file:
        data = json.load(json_file)[0]  # Load only the first set of data

    # Read XPath data from the JSON file
    with open('../data/create_accnt_xpath.json') as xpath_file:
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

    # Click on the create_button
    if 'create_btn' in xpath_dict:
        create_btn_xpath = xpath_dict['create_btn']
        create_btn = self.driver.find_element(By.XPATH, create_btn_xpath)
        create_btn.click()

    # Add the 'registered' field to the data
    data['registered'] = 'Yes'

    # Load existing registered data (if any) from 'registered.json'
    try:
        with open('../data/registered.json', 'r') as registered_file:
            registered_data = json.load(registered_file)
    except (FileNotFoundError, json.JSONDecodeError):
        registered_data = []

    # Append the newly created account data to the existing list
    registered_data.append(data)

    # Write the updated data to 'registered.json'
    with open('../data/registered.json', 'w') as registered_file:
        json.dump(registered_data, registered_file, indent=2)

    # Delete the data from signup_data.json
    with open('../data/signup_data.json', 'r') as json_file:
        used_data = json.load(json_file)

    used_data.pop(0)  # Remove the first set of data
    with open('../data/signup_data.json', 'w') as json_file:
        json.dump(used_data, json_file, indent=2)
