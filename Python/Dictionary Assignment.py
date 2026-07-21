print("===========================================================")
print("           Question 1 — Student Profile System             ")
print("===========================================================")

student = {
    "name": "Noor Fatima",
    "age": 16,
    "city": "Karachi",
    "hobbies": ["Reading", "Coding","Cooking"],
    "skills": ["Python", "Video Editing", "Procedural Programming"]
}

print("Student name:", student["name"])
print("First hobby:", student["hobbies"][0])
print("Total skills:", len(student["skills"]))

print("==============================================================")
print("             Question 2 —Student Marks System                 ")
print("==============================================================")

student = {
    "name": "Noor Fatima",
    "age": 16,
    "marks": {
        "english": 50,
        "math": 80,
        "science": 60,
        "computer": 10
    }
}

total_marks = student["marks"]["english"] + student["marks"]["math"] + student["marks"]["science"] + student["marks"]["computer"]

average_marks = total_marks / len(student["marks"])

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

print("===============================================================")
print("                Question 3 — Grade Checking System             ")
print("===============================================================")

average = 82

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)

if average >= 60:
    print("Passed")
else:
    print("Failed")
    
print("================================================================")
print("           Question 4 — Attendance Management System            ")
print("================================================================")

attendance = {
    "total_classes": 100,
    "attended_classes": 80
}

percentage = (attendance["attended_classes"] / attendance["total_classes"]) * 100

print("Attendance:", percentage, "%")

if percentage < 75:
    print("Short Attendance")
else:
    print("Eligible For Exam")
    
print("==============================================================")
print("            Question 5 — Fee Management System                ")
print("==============================================================")

fee_status = {
    "fee_paid": True
}

if fee_status["fee_paid"]:
    print("Fee Cleared")
else:
    print("Fee Pending")
    
print("================================================================")
print("             Question 6 — Skills Management System              ")
print("================================================================")

user_data = {
    "skills": ["Python", "HTML", "CSS"]
}

user_data["skills"].append("JavaScript")
user_data["skills"].remove("HTML")

print("Updated Skills List:", user_data["skills"])
print("Total Skills:", len(user_data["skills"]))

print("============================================================")
print("           Question 7 — Login Authentication System         ")
print("============================================================")

login_info = {
    "username": "Hasnain",
    "password": "Zone_x"
}

user_name = input("Enter username: ")
user_password = input("Enter password: ")

if user_name == login_info["username"] and user_password == login_info["password"]:
    print("Login Successful")
else:
    print("Invalid Credentials")
    
print("==============================================================")
print("            Question 8 — Address Management System            ")
print("==============================================================")

address = {
    "area": "Gulshan",
    "street": "Street 5",
    "house_number": "A-12"
}

print(address["area"], address["street"], address["house_number"])

address["area"] = "North Nazimabad"
address["zip_code"] = "74700"

print(address)

print("===============================================================")
print("            Question 9 — Multiple Students Database            ")
print("===============================================================")

students = {
    "student1": {
        "name": "Ali",
        "city": "Karachi",
        "marks": 450
    },
    "student2": {
        "name": "Ahmed",
        "city": "Lahore",
        "marks": 420
    }
}

print("Student 1 Name:", students["student1"]["name"])
print("Student 2 Marks:", students["student2"]["marks"])

students["student2"]["city"] = "Islamabad"

print(students)

print("=================================================================")
print("         Question 10 — Final Student Report Card System          ")
print("=================================================================")

student = {
    "profile": {
        "name": "Noor Fatima",
        "age": 16,
        "city": "Karachi"
    },
    "marks": {
        "math": 80,
        "english": 75,
        "science": 85,
        "computer": 90
    },
    "attendance": 80,
    "fee_status": "Paid",
    "skills": ["Python", "HTML", "CSS"],
    "address": {
        "area": "Gulshan",
        "street": "Street 5",
        "house_number": "A-12"
    }
}

total = 80 + 75 + 85 + 90
average = total / 4

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

print("----- Report Card -----")
print("Name:", student["profile"]["name"])
print("City:", student["profile"]["city"])
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
print("Attendance:", student["attendance"], "%")
print("Fee Status:", student["fee_status"])
print("Skills:", student["skills"])
print("Address:", student["address"]["area"], student["address"]["street"], student["address"]["house_number"])
