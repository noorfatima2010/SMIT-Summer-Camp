print("----------------------------------------------")
print("         Question 1 — ATM Machine System      ")
print("----------------------------------------------")

# Input
balance = int(input("Enter your account balance: "))
withdraw = int(input("Enter your withdraw amount: "))

# Condition check
if withdraw > balance:
    print("Insufficient Balance")
elif withdraw < 500:
    print("Minimum withdrawal is 500")
else:
    balance = balance - withdraw
    print("Remaining Balance: ",balance)
if balance > 10000:
    print("Premium User")
else:
    print("Normal User")

print("----------------------------------------------")
print("     Question 2 — Smart Username Validator    ")
print("----------------------------------------------")

# Input
username = input("Enter your username: ")

# Condition check
if len(username) <= 8:
    print("Username must be at least 8 characters long")
elif " " in username:
    print("Username should not contain spaces")
elif not username[0].isupper():
     print("Username must start with a capital letter")
elif not any(char.isdigit() for char in username):
    print("Username must contain at least one number")
else:
    print("Username is valid")

print("----------------------------------------------")
print("     Question 3 — Exam Eligibility Checker    ")
print("----------------------------------------------")

# Input
name = input("Enter your student name: ")
attendance = float(input("Enter your attendance percentage :"))
fees = input("Enter your fees status (paid/unpaid): ")

# Condition check
if attendance >= 75 and fees.lower () == "paid" :
    print("Eligible for exam")
else:
     print("Not eligible for exam")
if attendance < 75:
        print("Reason: Low attendance")
if fees.lower() != "paid":
    print("Reason: Fees not paid")

print("-----------------------------------------------")
print("     Question 4 — Password Security Checker    ")
print("-----------------------------------------------")

password = input("Enter your password: ")
is_strong = True

if len(password) < 8 :
    is_strong = False
    print("Password length should be greater than or equal to 8")
elif password.find("@") == -1 and password.find("#") == -1 :
    is_strong = False
    print("Password must contain '@' or '#'")
elif password.find(" ") != -1 :
    is_strong = False
    print("Password should not contain spaces")
elif password[0].isupper() != True:
    is_strong = False
    print("First character should be uppercase")

if is_strong :
    print("Strong Password")
else:
    print("Weak password")

print("=====================================================")
print("     Question 5 — Online Shopping Discount System    ")
print("=====================================================")

customer_name = input("Enter customer name: ")
total_bill = float(input("Enter total bill: "))
membership_status = input("Enter membership status (yes/no): ").lower()

discount = 0

if total_bill > 5000 and membership_status == "yes":
    print("Apply 20% discount")
    discount = total_bill * 0.20
elif total_bill > 3000:
    print("Apply 10% discount")
    discount = total_bill * 0.10
else:
    print("No discount")

final_bill = total_bill - discount
print("Final_bill:", final_bill)

print("=======================================================")
print("        Question 6 — Email Verification System         ")
print("=======================================================")

email = input("Enter your email: ")

is_email = email.endswith("@gmail.com")
not_space = " " not in email
lenght = len(email) > 12

print("Valid gmail:",is_email)
print("Not space:",not_space)
print("Lenght:",lenght)

valid = is_email and not_space and lenght

if valid:
    print("Email Verified")

else:
    print("Invalid Email")
    
print("=========================================================")
print("         Question 7 — Smart Number Analyzer              ")  
print("=========================================================") 

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("zero")

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

if num % 5 == 0:
    print("Divisible by 5")
    
if num > 100:
    print("Large Number")

print("===========================================================")
print("         Question 8 — Truthy Falsy Login System            ")
print("===========================================================")

username = input("Enter username: ")
password = input("Enter password: ")

if username and password:
    print("Login Attempted")
    
else:
    print("Fields Cannot Be Empty")
    
print(username.lower())
print(username[::-1]) 

print("=============================================================")
print("              Question 9 — Word Analyzer System              ")
print("=============================================================")
    
sentence = input("Enter a sentence: ")
if 'Python' in sentence:
    print("Python Found")
    
if len(sentence) > 20:
    print("Long Sentence")
    
else:
    print("Short Sentence")
sentence = sentence.replace("Python","JavaScript")

print(sentence[::-1])
    
print("=======================================================")
print("       Question 10 — Nested Login & Role Checker       ")
print("=======================================================")

username = input("Enter username: ")
password = input("Enter password: ")
role = input("Enter role (admin/student): ")

if len(username) == 0:
    print("username is empty")
if len(password) == 0:
    print("password is empty")
else:
    # Nested If Else
    if role == "admin":
        print("welcome admin")
    elif role == "student":
        print("welcome student")
    else:
        print("Invalid Role")
    
