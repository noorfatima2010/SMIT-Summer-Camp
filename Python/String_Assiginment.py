print("============================================")
print("1. Professional Email Management System     ")
print("============================================")
# employee email 
email = "ali.ahmed2026@softwarehouse.com"
# username
username = email.split('@')[0]
# company name
company = email.split('@')[1]
# domain extension
extension = email.split(".")[-1]
# email without domain extension
email_without_extension = email.rsplit(".", 1)[0]
# first 12 characters of email
first_12_characters = email[:12]
# last 10 characters of 
last_10_characters = email[-10:]

#Print
print("Username:", username)
print("Company Name:", company)
print("Domain Extension:", extension)
print("Email Without Domain Extension:",email_without_extension)
print("First 12 Characters Of Email:",first_12_characters)
print("last 10 Characters Of Email:", last_10_characters)

print("===============================================")
print("2.    E-Commerce Product Code Analyzer         ")
print("===============================================")
# Product
product = " MOB-APPLE-IPHONE15PRO-256GB-BLACK"

# Split product code into parts
parts = product.split("-")
# Print Product category
print("Category:", parts[0])
# 2. Print company name
print("Company:", parts[1])
# 3. Print model name
print("Model:", parts[2])
# 4. Print storage size
print("Storage:", parts[3])
# 5. Print product color
print("Color:", parts[4])
# 6. Print first character of company name
print("First character of company name:", parts[1][0])
# 7. Print last character of model name
print("Last character of model name:", parts[2][-1])

print("===============================================")
print("3.         Online Banking SMS Processor        ")
print("===============================================")
# Store SMS in variable
sms = "PKR 25000 has been successfully transferred to account 45892" 

# Split SMS into words
words = sms.split()

# print transferred amount only
print("Transfer Amount:", words[1])
# print account number only
print("Account Number:", words[-1])
# print transaction status word only
print("Transaction Status:", words[4])
# print first 25 characters
print("First 25 Characters:", sms[:25])
# print last 15 characters
print("Last 15 Characters:", sms[-15:])
# count how many times letter "a" appears
count_a = sms.lower().count("a")
print("Count of 'a':", count_a)

print("==============================================")
print("4.    University Student Record Formatter     ")
print("==============================================")
# student data 
data = "BSCS|2026|'045'|Muhammad Ali Ahmed"
# print department name
print("Department Name:", data[0:4])
# print batch year
print("Batch Year:", data[5:9])
# print roll number
print("Roll Number:", data[11:14])
# print student full name
print("Student Full Name:", data[16:35])
# print only first name
print("First Name:", data[16:23])
# print initials of student name
print("Initials Of Student Name:", data[-18] + data[-9] + data[-5])

print("================================================")
print("5.       Website URL Processing System          ")
print("================================================")
# Website URL
url = "https://www.amazonshoppingstore.com"

# remove "https://"
print("Without https://:", url[8:])
# remove "www."
print("Without www.:", url[12:])
# print website name only
print("Website name:", url[12:-4])
# print domain extension
print("Domain extension:", url[-3:])
# check whether URL ends with ".com"
print("Ends with .com:", url[-4:] == ".com")
# print middle portion of URL using slicing
print("Middle portion:", url[8:-4])

print("=============================================")
print("6.        Secure Password Formatter          ")
print("=============================================")
# store password
password = "Noor@123456"

# print hidden password format
print("Hidden Password:", "*" * len(password))
# print first character
print("First Character:", password[0])
# print last character
print("Last Character:", password[-1])
# print total password length
print("Password Length:", len(password))
# print middle characters using slicing
print("Middle Characters:", password[1:-1])
# check whether password ends with a specific number
print("Ends with 6:", password[-1] == "6")

print("==============================================")
print("7.          File Management System            ")
print("==============================================")
# store filename
file = "python_final_project_documentation_2026.pdf"

# 1. replace underscores with spaces
print("Formatted Name:", file.replace("_", " "))
# 2. print filename without extension
print("Filename without extension:", file[:-4])
# 3. print extension only
print("Extension:", file[-3:])
# 4. check whether file is PDF
print("Is PDF File:", file[-4:] == ".pdf")
# 5. print first 20 characters
print("First 20 characters:", file[:20])
# 6. print last 10 characters
print("Last 10 characters:", file[-10:])

print("==============================================")
print("8.      Social Media Username Generator       ")
print("==============================================")
# store data
first_name = "noor"
last_name = "fatima"
game = "freefire"
lucky_number = "4"

# create username
username = first_name + "_" + last_name + "_" + game + "_" + lucky_number
print("Full Username:", username)
# username without lucky number
print("Without Lucky Number:", username[:-2])
# only game name
print("Game Name:", username.split("_")[2])
# only lucky number
print("Lucky Number:", username.split("_")[-1])
# first 8 characters
print("First 8 characters:", username[:8])
# last 6 characters
print("Last 6 characters:", username[-6:])
# capitalize format
print("Capitalized:", username.title())

print("==============================================")
print("9.       Chat Message Analyzer System         ")
print("==============================================")
# store message
msg = "hello Teacher i have completed my python assignment successfully"

# capitalize the message
print("Capitalized Message:", msg.capitalize())
# replace python with javascript
print("Replaced Message:", msg.replace("python", "javascript"))
# find position of assignment
print("Position of 'assignment':", msg.find("assignment"))
# count how many times "s" appears
print("Count of 's':", msg.count("s"))
# first 18 characters
print("First 18 characters:", msg[:18])
# last 20 characters
print("Last 20 characters:", msg[-20:])
# print only word "completed"
print("Word 'completed':", msg[16:25])

print("==============================================")
print("10.     Online Course Information System      ")
print("==============================================")
# Course information
course = "Python Programming Complete Bootcamp 2026"

# print course name only
print("Course name:", course[0:-4])
# print batch year only
print("Batch year:", course[-4:])
# print first word
print("First word:", course[0])
# print last word
print("Last word:", course[-1])
# print first 15 characters
print("First 15 characters:", course[0:-26])
# print last 12 characters
print("Last 12 characters:", course[-12:])
# count how many times letter "o" appears
print("Count of 'o':", course.count("o"))
# check whether title ends with "2026
print("Ends with 2026:", course.endswith("2026"))

