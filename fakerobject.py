from faker import Faker
import json
import posttest

class person():
    
    def __init__(self, lang="en_US"):
        fake = Faker(lang)
        self.name = fake.name()
        self.age = fake.random_int(1,100)
        self.address = fake.address()
        self.credit_card = fake.credit_card_number()
        self.company = fake.company()
        self.job = fake.job()
        self.phone_number = fake.phone_number()
        self.email = fake.email()

    def json_generator(self):
        data = [{
            'name': self.name,
            'age': self.age,
            'address': self.address,
            'credit_card': self.credit_card,
            'company': self.company,
            'job': self.job,
            'phone_number': self.phone_number,
            'email': self.email}]

        return json.dumps(data)

def json_formatter(data):
    return json.dumps(data,indent=4,separators=(',', ': '))

if __name__ == "__main__":
    #for _ in range(10):
    person1 = person()
    person1_json = person1.json_generator()
    res = posttest.posting(person1_json)

    print(json_formatter(res.json()))
