print("=======================================================") 
print("                  Using While Loop                     ")
print("=======================================================")

# 1. print numbers from 1 to 100.

count = 1
while count <= 100:
    print(count)
    count = count + 1
    
# 2. print number from 100 to 1.

count = 100
while count >= 1:
    print(count)
    count = count - 1
    
# 3. print the multiplication table of a number n.

count = 1
table = 5

while count <= 10:
    print(table * count)
    count = count + 1
    
# 4. print the elements of the following list using a loop.

numbers = [12,45,8,23,67,34,90,15,56,78]
list_length = len(numbers)
i = 0
while (i< list_length):
    print(numbers[i])
    i += 1
    
# 5. Search for a number x in this tuple using loop.

numbers = (18, 45, 72, 91, 34, 56, 29, 83, 67, 10)
list_len = len(numbers)

i = 0
while (i < list_len):
    print(numbers[i])
    i = i + 1
    
# 6. Write a program to find the sum of first natural numbers.

i = 1
total = 0
while i <= 5:
     total + i
     i = i + 1
        
print(total)

print("=========================================================")
print("                     Using For Loop                      ")
print("=========================================================")

# 1. Print the elements of the following list using a loop.

fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes', 'Peach', 'Cherry', 'Guava',
'Pineapple', 'Watermelon']

for fruit in fruits:
    print(fruit)

# 2. Search for a string x in this tuple using loop.

cities = ('Karachi', 'Lahore', 'Islamabad', 'Peshawar', 'Quetta', 'Multan', 'Hyderabad',
'Faisalabad', 'Sialkot', 'Sukkur')

x = "Lahore"

for city in cities:
    if city == x:
        print(city)
        break

# 3. Write a program to find the factorial of first natural numbers.

numbers = [1,2,3,4,5]
factorial = 1
for num in numbers:
    factorial *= num
print(factorial)

print("=========================================================")
print("                      Using range()                      ")
print("=========================================================")

# 1. Print numbers from 1 to 100.

for number in range(1 , 101):
    print(number)

# 2. Print numbers from 100 to 1.

for numbers in range(100 ,0, -1):
    print(numbers)
    
# 3. Print the multiplication table of a number n.

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
