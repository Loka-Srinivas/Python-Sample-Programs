# 05/08/2025
# LOOPS AND CONTROL STATEMENTS IN PYTHON:-


# TASKS AND BREAK:-


def first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return None

print(first_even([1, 3, 7, 8, 9]))  # Output: 8


correct = "1234"
tries = 0

while tries < 3:
    pwd = input("Enter password: ")
    if pwd == correct:
        print("Access granted")
        break
    else:
        print("Wrong password")
        tries += 1
else:
    print("Locked out")


while True:
    text = input("Type something (or 'exit' to stop): ")
    if text == "exit":
        break
    print("You typed:", text)

# TASKS AND BREAK:-


nums = [3, -1, 5, -7, 9]
for n in nums:
    if n < 0:
        continue
    print(n)


word = "education"
for ch in word:
    if ch in "aeiou":
        continue
    print(ch, end=" ")


for i in range(1, 51):
    if i % 3 == 0 and i % 5 != 0:
        print(i)


# TASKS ON PASS:-

def process_data():
    pass


class User:
    pass


for i in range(1, 6):
    pass


nums = [0, 12, 25, 0, 44, 55, 60, 2]

for n in nums:
    if n == 0:
        pass
    elif n % 2 != 0:
        continue
    elif n >= 50:
        break
    print(n)


words = ['hi', 'cat', 'wait', 'dog', 'end', 'zebra']

for w in words:
    if len(w) < 3:
        continue
    elif w == "end":
        break
    elif w == "wait":
        pass
    print(w)
