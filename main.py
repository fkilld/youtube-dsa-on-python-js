# Positive or Negative number: C | C++ |  Java | Python
# def positive_negative(n):
#     if n>0:
#         # print('positive number')
#         return 'positive number'
#     else :
#         # print('negative number')
#         return'negative number' 

# print(positive_negative(9))


# Even or Odd number: js | Python
# def even_odd(n):
#     if n%2==0:
#         return 'even'
#     else:
#         return 'odd'

# print(even_odd(12))
# print(even_odd(13))
# Sum of First N Natural numbers:  js | Python

# def sumOfFirst(n):
#     i = 1
#     sum = 0
#     while i<=n:
#         sum+=i
#         i+=1
#     return sum
    
# print(sumOfFirst(12))

# Sum of N natural numbers:  js | Python

# Sum of numbers in a given range: js  | Python
# def sumofNumber(s,e):
#     sum = 0 
#     while s<=e:
#         sum+=s
#         s+=1
#     return sum
# print(sumofNumber(2,5)) # 14
# Greatest of two numbers: js | Python
# def greatest_of_two(a,b):
#     if a> b :
#         return 'a is greater'
#     else :
#         return 'b is greater'

# print(greatest_of_two(5,10))
# Greatest of the Three numbers: js | Python
# def greatest_of_three(a,b,c):
#     if a> b and a> c :
#         return 'a is greater'
#     elif b> c and b> a :
#         return 'b is greater'
#     else :
#         return 'c is greater'

# print(greatest_of_three(5,10,12))
# Leap year or not: js | Python
# Divisible by 4 → If a year is divisible by 4, it is a leap year.
# ✅ Example: 2024, 2028, 2032

# Exception - Century Years → If a year is divisible by 100, it is not a leap year, unless it is also divisible by 400.
# ❌ Example: 1700, 1800, 1900 (Not leap years)
# ✅ Example: 1600, 2000 (Leap years)

# def is_leap_year(year):
#     if (year % 400==0)or (year % 4==0 and year % 100!=0):
#         return f'{year} is a leap year'
#     else :
#         return f'{year} is not a leap year'
        
# print(is_leap_year(2018))



# Prime number: js | Python
# def prime_number(n):
#     if n <= 1:
#         return False
#     i ,flag =2,True
#     while i<n:
#         if n%i==0:
#             return False
#         i+=1
#     return flag
# print(prime_number(12))
# def prime_number(n):
#     if n <= 1:
#         return False
#     i ,flag =2,True
#     while i*i<n:
#         print(i)
#         if n%i==0:
#             return False
#         i+=1
#     return flag
# print(prime_number(15))

# Prime number within a given range: js | Python
# def prime_number(n):
#         i = 2        
#         while i<= n:
#             flag = True
#             j =2
#             while j*j <=i:
#                 if i % j ==0:
#                     flag = False
#                     break
#                 j+=1
#             if flag:
#                 print(i,'is a prime number')
#             i+=1

# prime_number(15)
# Sum of digits of a number: js | Python
# Reverse of a number : js | Python
# Palindrome number: js | Python
# Armstrong number : js | Python
# Armstrong number in a given range : js | Python
# Fibonacci Series upto nth term : js | Python
# Find the Nth Term of the Fibonacci Series : js | Python
# Factorial of a number : js | Python
# Power of a number : js | Python
# Factor of a number : js | Python
# Finding Prime Factors of a number : js | Python
# Strong number : js | Python
# Perfect number : js | Python
# Perfect Square : js | Python
# Automorphic number : js | Python
# Harshad number : js | Python
# Abundant number : C| C++ | Java | Python
# Friendly pair : C | C++ |   Java | Python