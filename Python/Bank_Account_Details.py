#Bank_Information
bank_name = "Habib bank"
branch_name = "Gulshan-e-iqbal"
branch_code = 1549
city = "karachi"

#Customer_Information
customer_name = "ali ahmed"
father_name = "m.mubeen"
age = 21
phone_number = "03152083559"
email_address = "aliahmedyk18@gmail.com"

#Account_Information
account_number = 123456789
account_type = "saving account"
currency = "PKR"
account_balance = 85000
loan_amount = 250000
atm_card_number = 987654321

#Account_status
account_active_status = True
loan_approved_status = False

print("="*100)

print("==================================================")
print("                 Habib_Bank                       ")
print("==================================================")

print("="*100)
print("welocome",customer_name,"to", bank_name)
print("customer_name","from", city,"has opened a", account_type)
print("Father Name:" , father_name ,"|Age:" , age)
print("Branch Name:" , branch_name , "|Branch Code:" , branch_code)
print("Account Number:" , account_number , "|Card number:" , atm_card_number)
print("Phone number:" , phone_number , "| Email:" , email_address)
print("Current Balance:" , account_balance , currency)
print("loan amount approved:" , loan_amount , currency)
print("account active status:" , account_active_status)
print("loan approved status:" , loan_approved_status)
print(account_active_status)
print(loan_approved_status)
print("="*100)
                   
print("======================================================")
print("               Account_Information                    ")
print("======================================================")

print("="*100)
print("Old_Balance:" ,account_balance, currency)
print("Updated_Balance:" ,account_balance+loan_amount, currency)

print("="*100)
print(type(bank_name))
print(type(branch_name))
print(type(branch_code))
print(type(city))
print(type(customer_name))
print(type(father_name))
print(type(age))
print(type(phone_number))
print(type(email_address))
print(type(account_number))
print(type(account_type))
print(type(currency))
print(type(account_balance))
print(type(loan_amount))
print(type(atm_card_number))
print(type(account_active_status))
print(type(loan_approved_status))
