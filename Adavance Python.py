# # ADVANCED PYTHON:
    
# # Exception Handling:
# Error:
#    It is an interruption in our program which stops the flow of execution abruptly.
#    Types of errors:
       
# 1. Compile time error/syntax errors:
#     These  are the errors which occur during compiling a program.
      
#     EG: print("hello" world)
    
# 2. Exception/run-time errors:
    
#     These errors occur during execution/ run time interpretation of a program

# EG: print(10/0)   gives ZeroDivisionError
# list1=[1,2,3,4,5]
# print(list1[6])   

# In order to handle these exceptions so that the flow of execution of program 
# won't be interrupted we use a mechanism called exception handling. 

# For exception handling we use two main keywords: try and except.

# try:
# In try block we write the code which has the possibility of raising an exception.Exception

# except:
# In this block we write the code that should happen when an exception is occurred.

# We cannot write a try block without an except block.

# Syntax:
# try:
#     # block of code which may raise an exception.
    
# except:
#     # block of code to handle the exception.     
        
# try:        
#     num1=int(input("Enter a number:"))
#     num2=int(input("Enter another number:"))
#     # 
#     div=num1/num2
#     print("The division is:",div)
     
# except ZeroDivisionError:
#      print("Cannot divide a number by zero")
     
# print("Exception continued even after an exception occurred / handling")   

# # Handling Index Error:

# try:
#     list1=[1,2,3,4,5]
#     indVal=int(input("Enter the index val of the number:"))
#     print(list1[indVal])
# except IndexError:
#     print("Hightest index value availble is 4")    
    
# By default an except block witha specified error can only handle that one error. 
# If your program can raise multiple types of exceptions then your program might need multiple except blocks to handle those exceptions.

# except ValueError:
#      print("please provide interger value only")      

     
     
# TASK:

# list1=[2,3,4,5,'Lokanath',6,7,8]
# perform sum of the list and also handle the error with exception handling.

# list1=[2,3,4,5,'Lokanath',6,7,8] 
# sum1=0
# for i in list1:
#     sum+=i
#     print("Sum")
# _________________________________________________________________________________________

# 19/11/2025

# Though this type of exception handling is easy it is not advisable as it is not specifying what exactly went wrong.

# In case if i dont know the type of error but I want to know what exactly went wrong 
# in that case I can access that exception with a variable and print that exact error message.

# ______________________________________________________________________
# 20/11/2025:
# 
# Exception Handling:
# Finally:
# This block is excepted whether an exception is raise or not.
        
# try:
#     list1=[1,2,'3',4,5]
#     sum=0
#     for i in range(len(list1)):
#         sum+=list1[i] 
#     print(sum)
    
# except (TypeError, IndexError)as e:
#     print('Either you entered a wrong index or wrong value or you tried to add a number out of range')
    
# finally:
#     print("The program exception has been completed")               
        
           
     
# try:
#     list1=[1,2,'3',4,5]
#     sum=0
#     for i in range(len(list1)):
#         sum+=list1[i+1] 
#     print(sum)
    
# except (TypeError, IndexError) as e:
#     print("e")
    
# finally:
#     print("The program exception has been completed")   
    
# Difference between else and finally:
# else executes when no exception is raised where as finally excecutes
# whether an exception is raised or not.

       
# try:
#     num=int(input("Enter a number:"))
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
            
            
#     if count==2:
#         print("prime")
        
#     else:
#         print("Not Prime")
        
# except ValueError:
#     print("Enter a number instead of a string")                    
                    
 
 # raise Keyword:
# It is used to raise an exception manually.
# We can raise which ever type of existing error, with an custom message using a raise keyword.  


# age=int(input("Enter a number:"))
# if age>18:
#   print("Major")
    
# else:
#     raise KeyError("person must be above 18")  


#                 #  OR
# try:
#     age=int(input("Enter a number:"))

#     if age>18:
#      print("Major")
    
#     else:
#        raise KeyError("person must be above 18")  

# except NameError as e:
#     print(e)

#__----------------------------------------------------------------

#24/11/2025   

# Exception Handling:- 
  # raise KEYWORD:      
  # It is used toraise exception manually
# try:
#   age=int(input("Enter the number:"))
  
#   if age<18:
#     raise ValueError("Age must be a grether than 18 ")
#   print(age)
  
# except ValueError as e:
#   print(e)  


# Creating custom exceptions:-

#  We create custom exceptions so that we can debug large projects efficiently.
 
 
# class VenkatError(Exception):
#   pass

# raise VenkatError("I am raise this error out of no reason")

#We can create a custom exception by creating a class which inherits the exception class.


#Write a program such that if my list is empty than a custom exception must be raised.

# class ListError(Exception):
#   pass
# try:
#   list1=[]   
#   if len(list1)<0:
#     raise ListError("list cannot be empty")
#   print(list1)
  
# except ListError as e:
#   print(e)  

#Write a program to create an exception LowBalanceError and raise it when balance is less than 500

# class LowBalanceError(Exception):
#   pass
    
# try:
#     balance=int(input("Enter the balance:"))
#     if balance<500:
#       raise LowBalanceError("Your balance is below 500")
#     print(balance)
  
# except LowBalanceError as e:
#   print(e)    
  
  
# It is also used to raise an exception just like raise but assert exception is raised when the condition passed to its turns False.as_integer_ratio.


# assert Keyword:-

# raise KeyError("raising this to check")

# try:
#   name=input("Enter the name:")
#   assert len(name)>10, "Name must be atleast 10 character"
  
# except AssertionError as e:
#  print(e)
  
# Assert is generally used to debug or to evaluate conditions in our program.

# Write a program to check the validity of username and password, If username is wrong
# raise an customized UsernameError and if password is wrong then raise customized exception PasswordError.

# ____________________________________________________________________________________________________
#25/11/2025
  # EXCEPTION HANDLING:
    
#1.Chained Exception:-

  #  Raising another exception inside an exception.
  #  Here one Exception is raised from logging import exception.
  #  We use from keyword to show the connection between two exceptions.
  
        #EXAMPLE-1: 
        
# class ConnectivityError(Exception):
#   pass

# def conTime():
#   raise TimeoutError("Connection Timed Out")

# try:
#   conTime()
  
# except TimeoutError as e:
#   raise ConnectivityError("Cannot connect to the database") from e

         #EXAMPLE-2:
            
# class ConfigError(Exception):
#   pass
# try:
#   raise FileNotFoundError("Configuration file not found")

# except FileNotFoundError as e:
#   raise ConfigError("Configuration file not found") from e

  
#2. LOGGING :-
    # Storing error in a file so that you  can resolve them later.
    # Logging creates a file when it is not existing, if it already exists then it simply opens. 
    # It and write the error into it.
    
# import logging
# logging.basicConfig(filename="errors1.log")

# try:
#   list1=[1,2,3,4,5]
#   print(list1[10])
  
# except Exception as e:
#   logging.error(e)
  
# finally:
#   print("Logging Completed")  
# _______________________________________________________________________________
# #26/11/2025  

#ITERATORS:-

# Iterable and Iterate:-
# 1. Iterable:
#   It is a collection or sequence of data which can be converted into a iterator.
  
#   Eg:- string, list, tuple, set, dictionary, range, and file objects.
  
# list1=[1,2,3,4,5]
# # for i in list1:
# #   print(i)
  
# it1=iter(list1)

# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))
# except StopIteration:
#     print("The max value reached")  


# string1="venkat"

# strIte=iter(string1)

# try:
#   print(next(strIte))
#   print(next(strIte))
#   print(next(strIte))
#   print(next(strIte))
#   print(next(strIte))
#   print(next(strIte))

# except StopIteration:
#   print("Iterator exhausted!!") 
  
# dict1={'name':'venkat','qualification':'MCA','age':28}
# dictIte=iter(dict1)
# try:
  
#   print(next(dictIte))
#   print(next(dictIte))
#   print(next(dictIte))
#   print(next(dictIte))
#   print(next(dictIte)) 
  
# ranIte=iter(range(1,5))
# print(next(ranIter))       

    
# 2. Iterator:
#   Acessing/viewing all the values in a sequence one by one.

# 3. Iterator:
#   It is a collection of data where we access each value one at a time. 
  
#   Syntax:
#     iterName=iter(iterable)
#     next(iterName) 

# iter(): It converts an iterable into an iterator

# next(): Used to access each value in an iterator.


# fileName=open('path', encoding='UTF-8')
# print(next(fileopen))
# print(next(fileopen))



# By default every file object is an iterator.
# How/why: It contains both __iter__() and __next__() methods in it right away from creation.

# CONCULSION:-
            #  Anything that contains __iter__() and __next__() methods in it is an iterator.
            
# encoding:-
#           It is like a rulebook to my program which tells which pattern of binary values from which characters.
          
# UTF-8:-     UTF Stands For Unicode Transformation Format

#        It is universal language fromat which recognizes all the languages in the world. 
#_____________________________________________________                      
#27/11/2025

# next() Method:-

# Creating our own iterators:-

#    File object already has __iter__() and __next__() method in it so it is an iterator.
   
   #Hence, Anything that contains a __iter__() and __next__() in it is an iterator.
   
  #  Iterators are used to load chucks of huge data into memory and process them,
  #  so that huge file won't crash or lag the system.
     
# class EvenNumbers:
#   def __init__(self):
#     self.num=0
    
#   def __iter__(self):
#     return self  
  
#   def __next__(self):
#     self.num+=2
#     return self.num
  
# even=EvenNumbers() 
# print(next(even)) 
# print(next(even))
# print(next(even))
# print(next(even))
# print(next(even))


# class Stopwatch:
#   def __init__(self,num):
#     self.num=num
    
#   def __iter__(self):
#     return self  
  
#   def __next__(self):
#     if self.num<=0:
#       raise StopIteration
#     value=self.num
#     value-=1
#     return value
  
# watch=Stopwatch(10)

# print(next(watch))  
# print(next(watch))  
# print(next(watch))  
# print(next(watch))  
# print(next(watch))  
# print(next(watch))  

# Internally Opertator Works in for loop works.

# Eg:(-5,//5)
 #For loop runs internally based on iterators:
 
# list1=[1,2,3,4,5]
# for i in list1:
#   print(i)

# print("-----------------------------------------------------------")  
# it1=iter(list1)
# while True:
#   try:
#     i=next(it1) 
#     print(i)
    
#   except StopIteration:  
#       break   


filename=open("Copy path")

lines=filename.readlines()
for line in lines:
  print(line)