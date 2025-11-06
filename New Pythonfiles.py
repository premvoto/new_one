# # user details
name = input("Enter your name: ")
age = int(input("Enter your age: "))
location = input("Enter your location: ")
address = input("Enter your address: ")
salary = float(input("Enter your monthly salary: "))

annual_salary = salary * 12


print("\n--- User Details ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Location: {location}")
print(f"Address: {address}")
print(f"Monthly Salary: ${salary:.2f}")
print(f"Total Annual Salary: ${annual_salary:.2f}")