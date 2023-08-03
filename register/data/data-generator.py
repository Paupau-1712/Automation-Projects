import json
from faker import Faker
import random

signup_data_path = "register/data/signup_data.json"

fake = Faker()

countries = ["India", "United States", "Canada", "Australia", "Israel", "New Zealand", "Singapore"]

def generate_data(num_entries):
    data = []
    for i in range(num_entries):
        id_num = fake.uuid4()
        full_name = fake.name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        name_prefix = "Mr." if random.choice([True, False]) else "Mrs."
        name = f"{full_name}"
        email = fake.email().split('@')[0] + '@google.com'
        password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=80)
        month = birthday.month
        year = birthday.year
        company = fake.company()
        address = fake.address()
        country = random.choice(countries)
        state = fake.state() if country in ["India", "United States", "Canada", "Australia", "Israel", "New Zealand",
                                            "Singapore"] else None
        zip_code = fake.zipcode() if state else None
        city = fake.city() if state else None
        mobile_number = fake.phone_number()
        entry = {
            "id": id_num,
            "name": name,
            "first_name": first_name,
            "last_name": last_name,
            "name_prefix": name_prefix,
            "email": email,
            "password": password,
            "birthday": birthday.strftime("%d"),
            "month": month,
            "year": year,
            "company": company,
            "address": address,
            "country": country,
            "state": state,
            "zip_code": zip_code,
            "city": city,
            "mobile_number": mobile_number
        }
        data.append(entry)
    return data

if __name__ == "__main__":
    num_entries = 10000  # Change this number to generate more or fewer entries
    generated_data = generate_data(num_entries)

    # Save the data into a JSON file
    with open(signup_data_path, "w") as json_file:
        json.dump(generated_data, json_file, indent=2)

    print("Data generated and saved to 'generated_data.json'")