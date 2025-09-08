# 06/08/2025
# PROBLEMS OF LOOPS:-


for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)


while True:
    n = int(input("Enter number: "))
    if n % 11 == 0:
        print("First multiple of 11 entered:", n)
        break


text = input("Enter a string: ")
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Vowel count:", count)


i = 100
while i >= 2:
    print(i)
    i -= 2


while True:
    pwd = input("Enter password: ")
    if pwd == "admin123":
        print("Access Granted")
        break
    else:
        print("Wrong password, try again")


n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)


for i in range(10):
    n = int(input("Enter number: "))
    if n < 0:
        continue
    print("Positive:", n)


N = int(input("Enter N: "))
total = 0
for i in range(1, 2*N, 2):
    total += i
print("Sum of first", N, "odd numbers =", total)


for num in range(2, 51):
    prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")



total = 0
while True:
    n = int(input("Enter number (0 to stop): "))
    if n == 0:
        break
    total += n
print("Total Sum =", total)
