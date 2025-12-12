#write a program to print sum of prices of items from a list using a for loop:


'''prices=[120,250,300,150,200]
sum=0
for price in prices:
    sum+=price
print(sum)'''

#count and print the numbers of even and odd numbers in a list:

'''numbers=[10,25,30,47,52,61]
even_num=0
odd_num=0
for i in numbers:
    if i%2==0:
        even_num+=1
       
    else:
        odd_num+=1
       
print(even_num,i)
print(odd_num,i)'''


#find the max among a sequence of values:

'''values=[32,35,30,36,34,31,33]
num=0
for i in values:
    if i>num:
      num=i
print('biggest num:',num) '''


#to check wheather a give username and password are correct or not and if the user enter 3 times wrong 'your account is locked'  must be printed 
#username='admin'
#password='Admin@123'


'''limit=3
for i in range(limit):
     username=input("enter username:")
     password=input("enter a password:")
     if password=='admin@123' and username=='admin':
         print("access granted")  
         break  
     else:
         print("invalid")  
else:
    print('your acnt is locked')'''
    



'''i=0
while i<3:
     username=input("enter username:")
     password=input("enter a password:")
     if password=='admin@123' and username=='admin':
         print("access granted")  
         break  
     else:
         print("invalid")  
         i+=1
else:
    print('your acnt is locked')  '''''  


# Write a program to print discount of 100 rs to passwnger with seat numbers which are divisible of 3 and 5:

'''seatnumber=[5,25,13,15,27,55,11,30]
for i in seatnumber:
    if i%3==0 and i%5==0:
        print(i,"100 rupees discount")
    else:
        print(i,'no disount')   '''   
    


#to check wheather a given item is in your store or not. itmes=['apple','banana','capcicum','bread','onions'],
#  display wheather the item is available or not, pass the items using input functions.


'''user=input('what do you want:')
itmes=['apple','banana','capcicum','bread','onions']
for item in itmes:
   
    if user==item:
        print('yes we have',item)
        break
else:
        print(user,'not available')   '''

#print reverse of a string (with out buiult in function).

'''string=input("enter a name:")
reversed_string=string[::-1]
print(reversed_string) '''

#average of marks of a five students.

'''marks=[400,450,530,550,570]
intial=0
for i in marks:
    intial+=i
    avg=intial//2
print('average value:',avg)'''


#check whether the given sides form a triangle or not:a=5, b=5, c=5
#(Triangle rule: sum of any two sides is greater than the third side)

'''side_a=int(input("enter a value:"))
side_b=int(input("enter b value:"))
hyp=int(input("enter hyp value:"))
sum=(side_a*2)+(side_b*2)
if hyp**2==sum:
    print('it is a triangle')
else:
    print('it is not an triangle') '''


#find a factorial of a given number

'''num=int(input("enter a num:"))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)'''


'''num=int(input("enter a num:"))
a=0
b=1
if num<0:
    print("enter a positive number")
elif num==b:
    print(b)
else:
    print(a,b,end=",") 
    for i in range(2,num):
        c=a+b
        print(c,end=',')
        a=b
        b=c

num=int(input('enter a number:'))
root=num**1/2
if root!=float:
    print('it is a perfect square')
else:
    print('it is not a perfect square')

num=input("enter a num:")
sum=0
for i in num:
    sum+=int(i)
print(sum)


num=int(input("enter a number:"))
sum=0
while num>0:
    dig=num%10
    sum+=1
    num=num//10
print(sum)


num=int(input("enter a number:"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)'''

'''num1=int(input('enter a num:'))
num2=int(input('enter a num:'))
num3=int(input('enter a num:'))

if num1>=num2 and num2>=num3:
    print('largest num:',num1)
elif num2>=num1 and num1>=num3:
    print('largest num',num2)  
else:
    print('largest num',num3) '''   


'''ovels=['a','e','i','o','u']
name=str(input("enter a name:"))
count=0
for i in ovels:
    for chr in name:
        if i==chr:
         count+=1
print(count)'''


'''num=input('enter a number:')
rev=num[::-1]
print(rev)'''

'''num=int(input("enter number:"))
if num%1==0 and num%2!=0 and num%3!=0:
    print('it is a prime number')
else:
    print('it is not a prime number') '''

'''num=int(input('enter a number:'))
for i in range(1,11):
    value=num*i
    print(f'{num}*{i}','=',value)  '''

'''num=int(input('enter a num:'))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)'''


'''for i in range(1,51):
    if i%3==0 and i%5==0:
        print(i,'fizzbuzz')
    elif i%3==0:
        print(i,'fizz')
    elif i%5==0:
        print(i,'buzz') 
    else:
        print(i,'not divisible')  '''    

'''name=str(input('enter a name:'))
rev=name[::-1] 
if name==rev:
    print('it is a palandrome')  
else:
    print('not a palandrome')  '''     


'''num=int(input("enter a num:"))
hour=num//60
minutes=num%60
print(f'{hour} hours and {minutes} minutes')'''

'''num=input('enter a number:')
sum=0
for i in num:
    sum+=int(i)
print(sum)'''


'''num=input("enter a number:")
count=0
for i in num:
    count+=1
print(count)  ''' 

'''num=int(input('enter a number:'))
for i in range(1,num+1):
    print(i)'''



'''def is_harshad(number):
    dig_sum=sum(int(digit) for digit in str(number))
    return number%dig_sum==0
num=18
if is_harshad(num):
    print(f'{num} is a harshad num')
else:
    print(f'{num} not a harshad number') '''      



'''def is_armstrong(number):
    dig=(int(digit) for digit in str(number))
    total=sum(digit**3 for digit in dig) 
    return total==number

for i in range(100,999):
    if is_armstrong(i):
        print(i)'''

'''def is_neon(n):
    square=n*n
    dig_sum=sum(int(d) for d in str(square))
    return dig_sum==n
print(is_neon(9))'''


'''def sunny(number):
    add=number+1
    root=add**1/2
    return root!=float
print(sunny(8))
'''


'''def factorial(n):
    if n==0 or n==1:
        return 1
    else:
       return n*factorial(n-1)
print(factorial(5))       
        '''

#rev of a string in a list

'''list1=['venkat','sai']
rev=[]
for word in list1:
    temp=''
    for char in word:
        temp=char+temp
    rev+=[temp]
print(rev)  
'''

# ''#armstrong number in an one list
# list1=list()
# for num in range(1,500):
#     dig=str(num)
#     num_dig=len(dig)
#     arm=sum(int(d)**len(dig) for d in dig)
#     if arm==num:
#         list1+=[num]
# print(list1)



# '''def fact(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num*fact(num-1)
        
# print(fact(5))   '''   

# '''def fibonacci_n(n):
#     a, b = 0, 1
#     for _ in range(n+1):
#         print(a,end=' ')
#         a, b = b, a + b

# print(fibonacci_n(10)) ''' # 10th Fibonacci number

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# # Print first 10 Fibonacci numbers
# for i in range(10):
#     print(fibonacci(i), end=" ")


'''for i in range(1,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
'''


#---------------------------------------------Problem Solving On Oops------------------------------------------------/

#1-------------------------------
'''class Shape:
    def area(self):
        print('This shape has no area')

class circle(Shape):
    def _init_(self,d):
        self.d=d
    def area(self):
        cal=3.14/4*(self.d**2)
        print(cal)
    

class Triangle(Shape):
    def _init_(self,len,brt):
        self.len=len
        self.brt=brt

    def area(self):
        cal=1/2*(self.len*self.brt)
        print(cal)

c1=circle(10)
c1.area()
T1=Triangle(5,6)
T1.area()


#2--------------------

class Student:
    def _init_(self,Name,Marks):
        self.name=Name
        self.Marks=Marks


    def Total(self):
        total=0
        for i in self.Marks:
            total+=i
        print(total)
        print(f'{self.name} has Scored The Marks {total}')
        return total
    
    def avg(self):
        count=0
        for i in self.Marks:
            count+=1
        print(f'No of Subjects Are {count}')
        average_marks=self.Total()//count
        print(f'{self.name} haa average of {average_marks}')
        return average_marks

    
   

s1=Student('venkat',[56,85,86,95,86])
s1.Total()
s1.avg()'''


#3----------------------------------

'''class Employee:
    def _init_(self,name,salary,increment):
        self.name=name
        self.salary=0
        self.setsalary(salary)
        self.increment=increment

    def setsalary(self,salary):
        if self.salary<0:
            print('The Salary canont be negative ')
        
        else:
            self.salary=salary

    def increment_salary(self,increment):
        incre='''


#-----------------------------------------

'''class Hotel:
    def _init_(self,name,price):
        self.hotel_name=name
        self.per_day_price=price

    def welcome(self):
        print(f'Welocme to {self.hotel_name}')


    def checkin(self):
        members=int(input('Enter date how many members are checkin:'))
        print(f'{members} members are checked in {self.hotel_name}')

    def checkout(self):
        days=int(input('How many days guests are stying:'))
        number_of_days=days
        print(f'{days} days are styed')
        return number_of_days
    

    def price_cal(self):
        total_amount=self.per_day_price*self.checkout()
        print(f'Total Bill: {total_amount}')

g1=Hotel('sai_hotel',500)
g1.welcome()
g1.checkin()
g1.checkout()
g1.price_cal()'''


#------------------------------------------------

'''
list1=[1,2,3,4,5,6,7,8,9]
num=int(input('index:'))
print(list1[num])'''


#----------------------------------------

'''list1=[]
limiit=10
for i in range(limiit):
    num=int(input('Num:'))
    list1+=[num]
print(list1)
'''

#-----------------------------------

''''
limit=10
for i in range(limit):
    list1=[]
    num=input('Num:')
    if num==int:
        list1+=[num]
        print(list1)
    else:
        continue
'''

#------------------------------------

'''l1=[1,2,3,4,5,6,7]
num=int(input('Num:'))
for i in l1:
    if i>num:
        break
else:
    l1+=[num]
print(l1)'''


#-----------------------------------

'''num=int(input('Num:'))
temp=num
rev=0
while temp>0:
    dig=temp%10
    rev=rev*10+dig
    temp//=10
if rev==num:
    print('Palindrome')
else:
    print('Not Palindrome')'''


#-------------------------------


'''text='a+((b-c)+d'
text1=''
for i in text:
    if i=='(' or i==')':
        continue
    else:
        text1+=i
print(text1)'''

#-----------------------------

'''l1=[1,2,3,4,5,8]
add=int(input('Num:'))
sum=0
for i in l1:
    if i>add:
        continue
    else:
        sum+=i
    if sum>=add:
        break
    else:
        print(sum)
    '''

#--------------------------


#1. Convert a temperature from celcius to farenheit.

'''c=int(input('Enter the temp in cell:'))
f=(c*9/5)+32
print('Faranite:',f)
        '''
# in function

'''def faranite(celcius):
    f=(celcius*9/5)+32
    print('Faranite:',f)
faranite(56)'''


#---------------------------

#2. caluculate net salary after adding allowences and removing deduction

'''basic_salary=int(input('basic salry:'))
allowences=int(input('Allowence:'))
deduction=int(input('Deduction:'))
total_salary=basic_salary+allowences-deduction
print('Total_salary:',total_salary)'''


#--------------------------------


#3. Find the area of circle


'''def area_circle(r):
    pi=3.14159
    area=pi*r**2
    print('Area Of circle:',area)
area_circle(10)
'''

#--------------------------

#4.caluculate simple intrest for an amount?

'''p_i=int(input('Principle amount:'))
r=int(input('intrest rate:'))
time=int(input('Enter time in years:'))
simple_intrest=(p_i*r*(time*12))/100
print('Simple_intrest:',simple_intrest)'''

#-------------------------

#5.cal avg marks of a student for 3 sub

'''maths=int(input('maths:'))
science=int(input('science:'))
social=int(input('social:'))
total_marks=maths+science+social
avg=total_marks//3
print('avg:',avg)'''

#--------------------------------

#6. swap a numbers


'''a=8
b=9
a,b=b,a
print(a,b)'''

#------------------------

#7. caluculate percentage of amount spent on groceries, bills and transport from a salary


'''salary=int(input('Salary:'))
grocery=int(input('Grocery:'))
bills=int(input('Bills:'))
trans=int(input("Transport:"))

total=grocery+bills+trans
per=(total/salary)*100
print('total_expences in percentage:',per)'''


#-----------------------------------


#8.cluculate speed of a bike: speed=distance(in terms of kilo)/time(in trems of hours)
     


'''def speed_bike(distance,time_in_min):
    dis=distance/1000
    hours=time_in_min/60
    speed=dis/hours
    print('speed of Bike:',speed)
speed_bike(200,10)'''


#9.Calculate age of person: age=current year-year of birth.

#10. Convert kilometers in to meters and centimerters 
# convert hours in to mintues and seconds.

# --------------------------------------------------------------

# 13/11/2025

# 1. Take a product name as string, it price as float, and quantity as int and create a bill by coverting the total price into a string.


'''ProductName=input("Enter the product name:")
Price=float(input("Enter the Price of the Product:"))
quantity=int(input("Enter the no of items:"))
totalPrice=Price*quantity
print(f'The Invoice of your purchases is {str(totalPrice)}')'''


# 2.Input: '_*_' and output:'_*_*_*_' Repulication


'''str1='_*_'          ''''string repulication''''
print(str1*3)'''


# 3. Take two numbers as strings and add then before and after type casting.

'''num1=input("Enter a number:")
num2=input("Enter another number:")
stradd=num1=num2
intadd=int(num1)+int(num2)
print(f'String addition is {stradd} and number addition is {intadd}')'''



# 4. Write a Program if temp is above 35c print temp its hot else print the temp is moderate.

    #    IF STATEMENT

'''temp=int(input("Enter the temp:"))
if temp>35:
    print("The temp is hot")
else:
    print("The temp is moderate")'''
    
# 5.# ELIF STATEMENT 
       
'''temp=int(input("Enter the temp:"))
if temp>35:
    print("The temp is hot") 
elif temp<=0:
    print("The temp is freezing")    
else:
    print("The temp is moderate")'''       

# 6.Write a program to check whether a person is eligible for vote or not.               

# Example:-1:

'''age=int(input("Enter your age:"))
Citizenship=input("Enter your citizenship:")
if age>=18 and Citizenship=="indian":
    print("You are Eligible to vote")
    
else:
    print("You are not Eligible to vote")'''
    
    
    
# 7.Write a program to give discount to a customer such that if he makes purchase of amount grather than 10000. He is eligible for 10% discount or else
#  no discount is available.
    #  Formule:
#  discount=percentage*totalamount/100 
 
'''Amount=int(input("Enter the total amount of bill:"))
 
if Amount>10000:
     discount=10*Amount/100
     Amount=Amount-discount
print(f'Your bill is {Amount}')  '''   
 

# 8. Check whether the sum of two digits is even or not. 

'''num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
sum="even" if (num1+num2)%2==0 else "odd"
print(f'The sum of two numbers is {sum}')'''
#__________________________________________________________ 
 #14/11/2025   
    
#1.  Write a program to check whether a year is leap year or not.
'''year=int(input("Enter the year:"))

if year %4==0 and year %100 !=0 or year %400==0:
    print(f'{year}is a leap year')
else:
    print(f'{year} is not a leap year')'''


#2. Evalute username and password such that if username is corect only then password.
# Input must be asked else it should return invalid username.    
        
'''username=input("Enter the username:")
if username=="admin":
    password=input("Enter the password:")
    if password=="admin@123":
        print("Access Granted")
else:
    print("Invalid Username")'''      
        
        
#3. Write a program to check whether a student is passed or faild. He should get min of 35 marks.
# In every subject and percentage must be greater than 40. else he is failed. (Take 3 subjects marks as input).  

#percentage=(sum of marks got in each subjects/sum of max marks in each subject)*100.   

'''sub1=int(input("Enter the marks of subject1:"))
sub2=int(input("Enter the marks of subject2:"))
sub3=int(input("Enter the marks of subject3:"))
total_marks=sub1+sub2+sub3
percentage=(total_marks/300)*100
if sub1>=35 and sub2>=35 and sub3>=35 and percentage>=40:
    print("you are passed")
else:
    print("you are failed")'''
    
    
#4. Write a program to print whether a person is eligible to get license or not using ternary.
#"value if condition is true " if condition else "value if condition is false"
'''age=int(input("Enter the age:"))
driving_test=input("Enter the driving test result Yes/No:")
result="Eligible for license" if age>=18 else "Not eligible for license"
print(result)
if age>=18:
    print("Eligible for license")
else:
    print("not eligible for license") '''  
    
#5. Write a program to check greatest among three numbers using ternary.
#"value1" if condition else "value2" if condition else "value3" 
'''num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))           
num3=int(input("Enter the third number:"))
gretest=num1 if num1>=num2 and num1>=num3 else num2 if num2>=num1 and num2>=num3 else num3
print(f'The gretest number is {gretest}')'''
           

class Account:
    def __init__(self, accountNumber, accountHolder, initialBalance):
        self.accountNumber = accountNumber
        self.accountHolder = accountHolder
        self.balance = initialBalance
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            return True
        return False
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            return True
        return False
    def transfer(self, amount, receiverAccount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            receiverAccount.balance = receiverAccount.balance + amount
            return True
        return False
    def showDetails(self):
        print("Account Number:", self.accountNumber)
        print("Account Holder:", self.accountHolder)
        print("Balance:", self.balance)
class Bank:
    def __init__(self, bankName):
        self.bankName = bankName
        self.accounts = []
    def createAccount(self, accountNumber, accountHolder, initialBalance):
        totalAccounts = 0
        for i in self.accounts:
            totalAccounts = totalAccounts + 1
        j = 0
        while j < totalAccounts:
            if self.accounts[j].accountNumber == accountNumber:
               return False
            j = j + 1
        newAcc = Account(accountNumber, accountHolder, initialBalance)
        self.accounts = self.accounts + [newAcc]
        return True
def findAccount(self, accountNumber):
    totalAccounts = 0
    for i in self.accounts:
        totalAccounts = totalAccounts + 1
    j = 0
    while j < totalAccounts:
        if self.accounts[j].accountNumber == accountNumber:
            return self.accounts[j]
        j = j + 1
    return None
def showAllAccounts(self):
    totalAccounts = 0
    for i in self.accounts:
        totalAccounts = totalAccounts + 1
    j = 0
    while j < totalAccounts:
        print("-----")
        self.accounts[j].showDetails()
        j = j + 1
bank = Bank("State Bank")
bank.createAccount(101, "Venkat", 5000)
bank.createAccount(102, "Pavan", 8000)
acc1 = bank.findAccount(101)
acc2 = bank.findAccount(102)
acc1.deposit(2000)
acc1.withdraw(1000)
acc1.transfer(1500, acc2)
bank.showAllAccounts()
          
    
       