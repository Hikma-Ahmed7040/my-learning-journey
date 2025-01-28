#part two
import time
print("Hello, world!"+"\n"+"Welcome to python programming")
#part three
time.sleep(1)
age = 25
height = 5.9
name = "John"
is_student = True
print(age, type(age))
time.sleep(1)
print(height, type(height))
time.sleep(1)
print(name, type(name))
time.sleep(1)
print(is_student, type(is_student))
time.sleep(1)
## i see the type keyword used to know what data types of variable holds

# we have to declare result variable because when num2 is zero the error will be happen
result= " "
#part three, i have done it before in advance
print("lets calculate numbers with basic arthimatic operation 😎🙈 and see my project☠️")
num1=int(input("enter the first numer: "))
num2=int(input("enter the second numer: "))
sign=input("sign(+,-,*,/): ")
if sign not in ["+","-","*","/"]:
     print("invalid operation")

if sign =="+":
      result = num1 + num2
elif sign=="-":
    result= num1 - num2
elif sign=="*":
     result= num1 * num2
elif sign=="/" and num2 ==0:
     print("error :division by zero!")
     
print(result)
time.sleep(1)
#part five :type conversion
# num="5"
# floated =float(num)
# print(floated + 7)
#bonus part  
name= input(" Hey type your name: ")
age= int(input("How old are you: "))
years=str(age)
city=input("Where are living: ")
print("Hello, "+name+"! you are "+years+" years old and live in "+city+".")
time.sleep(2)
#bonos two
current_year=2025
birthyear=current_year - age
#TO CONCATINATE THEM WE HAVE TO change int to str
BIRTHYEAR=str(birthyear)
print(" And your birth year is at "+BIRTHYEAR+" G.C")
time.sleep(3)

