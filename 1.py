# #adding two numbers
# # def add(a,b):
# #     c=a+b
# #     print(c)
# # add(2,6) #8
# # add(5,8) #13 

# #print hello world program
# # print("Hello world!")

# #calculate the sqrt of given number
# # def sqrrt(x):
# #     print(x**x)
# # sqrrt(2) #4
# # sqrrt(3) #9
# # sqrrt(4) #16
# # sqrrt(5) #25  

# #calculate the area of triangle 
# #1/2*b*h
# # def area(b,h):
# #     print((b*h)/2)
# # area(12,15) #90
# # area(13,15)  #97.5
# # area(14,15)  #105

# #swapping two variables in python

# # a=12
# # b=13
# # c=a
# # a=b

# # print(a)
# # print(c)

# #convert km to miles 
# # def km(a):
# #     print(a*0.621371)
# # km(1)
# # km(2) 
# # km(3)
# # km(4)
# # km(5)   

# #find the given number even or odd
# # number=int(input("Enter the number: "))
# # print(type(number))

# # def fin(number):
# #     if number==0 |number%2==0:
# #         print(number,"is an even number")
# #     else:
# #         print(number,"is an odd number")  
# # fin(0) #even 
# # fin(9) #odd
# # fin(20)   #even  
# # fin(325)  #odd   

# #leap year or not 
# # def lpyr(x):
# #     if x%100==0 and x%400==0:
# #         print(x,"is an leap year")
# #     elif x%4==0 and x%100!=0:
# #         print(x,"is a leap year")    
# #     else:
# #         print(x,"is not an leap year")    
# # lpyr(2004)
# # lpyr(2001)
# # lpyr(1997)
# # lpyr(2000)     
# # lpyr(2048) 
# # lpyr(1000) 

# #find the largest among 3 numbers 
# A=int(input("Enter the digit A: "))  
# B=int(input("Enter the digit B: "))
# C=int(input("Enter the digit C: "))

# if A>B and A>C:
#     print(A,"is greater than",B,C)
# elif B>A and B>C:
#     print(B,"is greaterthan",A,C)
# else:
#     print(C,"is greaterthan",A,B)  

#check weather a number is prime or not
# number=int(input("please enter the number : "))
# if number==1:
#     print(number,"is not a prime number")
# if number>1:        
#     for i in range(2,number):
#         if number%i==0:
#             print(number,"not a prime number")
#         else:
#             print(number,"is a prime number") 

#print 1 to 10 numbers
# for i in range(1,11):
#     print(i)

#print only factors of 3 till 30
# for i in range(1,30):
#         if i%3==0:
#            print(i)

#imprort a random number b/w 1 to 6
import random
print(random.randrange(1,7))