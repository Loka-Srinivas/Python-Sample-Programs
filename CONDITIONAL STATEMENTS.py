# 30/07/2025
# CONTROLS STATEMENTS IN PYTHON


num = int(input("Enter number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")


a = int(input("Enter first: "))
b = int(input("Enter second: "))
print("Greater is", a if a > b else b)


score = int(input("Enter score: "))
if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Fail")


n = int(input("Enter number: "))
if n > 0 and n % 2 == 0:
    print("Positive and Even")
else:
    print("Not matching")


age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teen")
else:
    print("Adult")
