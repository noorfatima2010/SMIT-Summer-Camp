print("====================================================")
print("           Food_Delivery_Bill_System                ")
print("====================================================")
# Food Delivery Bill System

# Prices 
burger_price = 300
pizza_price = 500

# Quantity 
burger_quantity = 2
pizza_quantity = 1

# Total food price 
total_food_price = (burger_price * burger_quantity) + (pizza_price * pizza_quantity)

# Delivery charges 
delivery_charges = 150

# Final bill 
final_bill = total_food_price + delivery_charges

# Print 
print("Total Food Price:", total_food_price)
print("Delivery Charges:", delivery_charges)
print("Final Bill:", final_bill)

print("====================================================")
print("              Student_Result_Calculator             ")
print("====================================================")
# Student Result Calculator

# Marks of 5 subjects 
math = 75
english = 60
chemistry = 80
physics = 70
computer = 85

# Total marks 
total_marks = math + english + chemistry + physics + computer

# Percentage
percentage = (total_marks / 500) * 100

# Pass/Fail
pass_status = percentage >= 50

# print
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Pass Status:", pass_status)

print("=====================================================")
print("            Online_Shopping_Discount                 ")
print("=====================================================")
# Online Shopping Discount

# original product price
original_product_price = 6000

# discount percentage
discount_percentage = 20

# discount amount
discount_amount = (original_product_price * discount_percentage) / 100

# final price after discount
final_price = original_product_price-discount_amount


comparison_result = final_price < 5000

# Print
print("Original Product:", original_product_price)
print("Discount Percentage:", discount_percentage)
print("Discount Amount:", discount_amount)
print("Final Price:", final_price)
print("Comparison Result:", comparison_result)

print("=====================================================")
print("                Bank_Account_Balance                 ")
print("=====================================================")
# current account balance
current_account_balance = 10000

# ATM withdrawal amount
atm_withdrawal_amount = 3000

# subtract withdrawal using assignment operator
current_account_balance -= atm_withdrawal_amount 

# mobile banking fee
bank_fee = 200

# subtract fee
current_account_balance -= bank_fee

# print
print("Withdrawal Amount:", atm_withdrawal_amount)
print("Banking Fee:", bank_fee)
print("Remaining Balance:", current_account_balance)

print("=====================================================")
print("                 Mobile_Login_Verification           ")
print("=====================================================")
# Mobile Login Verification

# username status
username_status = True

# password status
password_status = True

# fingerprint status
fingerprint_status = False

# login check (logical operator)
login_result = username_status and (password_status or fingerprint_status)

# print
print("Username Status:", username_status)
print("Password Status:", password_status)
print("Fingerprint Status:", fingerprint_status)
print("Login Result:", login_result)

print("=====================================================")
print("                   Car_Fuel_Average                  ")
print("=====================================================")
# Car Fuel Average

# total kilometers traveled
kilometers = 300

# total fuel used (liters)
fuel = 20

# average calculate (km per liter)
average = kilometers / fuel

# condition check
comparison_result = average >= 15

# print
print("Total Kilometers:", kilometers)
print("Fuel Used:", fuel)
print("Average (km/l):", average)
print("Good Average:", comparison_result)

print("=======================================================")
print("                 Employee_Salary_Management            ")
print("=======================================================")
# Employee Salary Management

# basic salary
employee_basic_salary = 50000

# bonus amount
bonus = 10000

# tax amount
tax = 5000

# add bonus using assignment operator
employee_basic_salary += bonus

# subtract tax using assignment operator
employee_basic_salary -= tax     

# final salary (after operations)
final_salary = employee_basic_salary

# print
print("Basic Salary + Bonus:", employee_basic_salary + tax - bonus)
print("Bonus:", bonus)
print("Tax:", tax)
print("Final Salary:", final_salary)

print("=======================================================")
print("                 University_Eligibility_Check          ")
print("=======================================================")
# University Eligibility Check

# student percentage
student_percentage = 72

# test status (True/False)
test_status = True

# eligibility condition (logical operator)
eligibility = (student_percentage >= 60) and test_status

# print results
print("Percentage:", student_percentage)
print("Test Status:", test_status)
print("Eligibility Result:", eligibility)

print("=========================================================")
print("                 Electricity_Bill_Calculator             ")
print("=========================================================")
# Electricity Bill Calculator

# number of electricity units
electricity_units = 250

# price per unit
per_unit_price = 25

# calculate total bill
total_bill = electricity_units * per_unit_price

# tax percentage
tax_percentage = 10

# calculate tax amount
tax_amount = (total_bill * tax_percentage) / 100

# final bill
final_bill = total_bill + tax_amount

# print results
print("Units:", electricity_units)
print("Unit Price:", per_unit_price)
print("Tax Amount:", tax_amount)
print("Final Bill:", final_bill)

print("=======================================================")
print("                Smartphone_Installment_System          ")
print("=======================================================")
# phone price
phone_price = 60000

# down payment
down_payment = 10000

# remaining amount
remaining_amount = phone_price - down_payment

# 12 months installment
monthly_installment = remaining_amount / 12

# comparison result
comparison_result = monthly_installment <= 5000

# print results
print("Phone Price:", phone_price)
print("Down Payment:", down_payment)
print("Remaining Amount:", remaining_amount)
print("Monthly Installment:", monthly_installment)
print("Comparison Result:", comparison_result)
