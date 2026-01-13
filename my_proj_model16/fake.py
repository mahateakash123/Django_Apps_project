
from faker import Faker

fake = Faker()  #creating object of faker class
for p in range(5):
    print("Employee First Name:",fake.first_name())
    print("Employee Last Name:",fake.last_name())
    print("Employee DOB",fake.date())
    print("Employee Email ID:", fake.email())
    print("EMployee ID:",fake.random_number(5))
    print("Employee Salary:", fake.random_int(min=10000, max=99999))
    print("EMployee Designation/Role:",fake.random_element(elements=('s/w Engineer','teamlead','manager','project Lead')))
    print("Employee Address:",fake.address())
    print("Employee City:",fake.city())
    print("=========================================END DETAILS=======================================================")