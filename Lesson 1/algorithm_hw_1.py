# Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

# #O(n)
n= int(input('enter a number: '))
result=0
if n !=0:
    for i in range (0,n +1):

        result = result+i
        print(result)

# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.
a=int(input('enter the first number:'))
b=int(input('enter the second number:'))
c=int(input('enter the third number:'))

#O(1)
if a>b and a>c:
        print(f'{a} is the largest')
elif b>a and b>c:
        print(f'{b} is the largest')
else:
    print(f'{c} is the largest')
#
# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

#O(n)
even=[]
odd=[]
number=(input('Enter a number: '))
for i in number:
    if int(i)%2 ==0:
        even.append(int(i))
    else:
        odd.append(int(i))
print(f'even:{even}')
print(f'odd:{odd}')