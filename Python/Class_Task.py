print("\n------ Student Profile System------")
name = input("Enter your name:")
age = input("Enter your age:")
city = input("Enter your city:")
course = input("Enter your course:")
total_marks = (input("Enter total marks:"))
obtained_marks = (input("Enter obtained marks:"))

# Convert marks into integer using int()
total_marks = int(total_marks)
obtained_marks = int(obtained_marks)

# Calculate percentage
percentage = (obtained_marks / total_marks) * 100

# Print all information in formatted style
print("\n-----------Student Profile-------------")
print("Name:",name)
print("Age:",age)
print("City:",city)
print("Course:",course)
print("Percentage :", str(int(percentage)) + "%")

# Show data types using type()
print("Name type:", type(name))
print("Age type:", type(age))
print("City type:", type(city))
print("Course type:", type(course))
print("Total Marks type:", type(total_marks))
print("Obtained Marks type:", type(obtained_marks))
print("Percentage type:", type(percentage))

print("\n------ Username Generator---------")
first_name = input("Enter your first name:")
last_name = input("Entre your last name:")
birth_year = input("Enter your birth year:")

# # Username banana (concatenation + lowercase)
username = (first_name + last_name + birth_year).lower()

# # Find username length using len()
length = len(username)

# # Print first and last character using indexing
first_character = username[0]
last_character = username[-1]

# #Output
print("\n---------- Username Details------------")
print("Username:",username)
print("Length:",length)
print("First Character:",first_character)
print("Last character:",last_character)

print("\n----------- Smart Calculator-------------")
# Take two numbers from user
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

# Operations
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
modulus = number1 % number2
power = number1 ** number2

# Output (formatted)
print("\n----- Smart Calculator -----")
print("Addition :", addition)
print("Subtraction :", subtraction)
print("Multiplication :", multiplication)
print("Division :", division)
print("Modulus :", modulus)
print("Power :", power)

print("\n--------- String Analyzer----------")
# Sentence
sentence = input("Enter a sentence:")

# Uppercase
print("Uppercase :", sentence.upper())
# Lowercase
print("Lowercase:",sentence.lower())
# Capitalize sentence
print("Capitalize:",sentence.capitalize())
# Count letter 'a' 
print("Count letter 'a':",sentence.count('a'))
# Replace words
print("Replace:",sentence.replace('a','b'))
# string using slicing
print("Reverse:",sentence[::-1])

print("\n-------- Email Checker System---------")
# Email
email = input("Enter your email: ")

# Check gmail 
is_email = email.endswith("@gmail.com")
# Username
username = email.split('@')[0]
# length
length = len(email)

# Output
print("Valid Gmail :", is_email)
print("Username :", username)
print("Length :", length)

print("\n------Shopping Bill Generator-------")
# Input
product = input("Enter product name: ")
price = int(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

# Total bill
total_bill = price * quantity
# Apply 10% discount
discount = total_bill * 0.10
# final bill
final_bill = total_bill - discount

# Output
print("Product:",product)
print("Quantity:",quantity)
print("Total Bill:",total_bill)
print("Discount:", int(discount))

print("\n-------— Mini Bio Data Card---------")
# User Information
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
course = input("Enter your course: ")

print("======================================")
print("           OUTPUT DETAILS             ")
print("======================================")

print("Name\t: " + name + "\nAge\t: " + age + "\nCity\t: " + city + "\nCourse\t: " + course)

print("\n-------Password Strength Checker---------")
# Paasword
password = input("Enter Password: ")
# Length
length = len(password)
contains_at = "@" in password

print("Password Length : " + str(length))
print("Contains @ : " + str(contains_at))
print("First 3 Characters : " + password[:3])

print("\n-------Movie Ticket System---------")

movie = input("Enter Movie Name: ")
price = int(input("Enter Ticket Price: "))
quantity = int(input("Enter Quantity: "))

# Calculate total amount
total = price * quantity

print("========================================")
print("                 RECEIPT                ")
print("========================================")

print("Movie : " + movie)
print("Tickets : " + str(quantity))
print("Total Amount : " + str(total))

print("\n-------Online Food Order Syste--------")

name = input("Enter Customer Name: ")
food = input("Enter Food Item: ")
price = int(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

# Calculate total bill
total = price * quantity
delivery = int(total * 5 / 100)
final_bill = int(total + delivery)

print("=====================================")
print("             RECEIPT                 ")
print("=====================================")

print("Customer : " + name)
print("Food Item : " + food)
print("Quantity : " + str(quantity))
print("Delivery Charges : " + str(delivery))
print("Total Bill : " + str(final_bill))
