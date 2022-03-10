# #compute sum of digits from 1 to n

# #O(n)
n= int(input('enter a number: '))
result=0
if n !=0:
    for i in range (0,n +1):
        result = result+i
print(result)
#
#
# #find max number from 3 values entered from keyboard
a= int(input('enter the first number: '))
b= int(input('enter the second number: '))
c= int(input('enter the third number: '))
#O(N)?>
if a>b and a>c:
        print(f'{a} is the largest')
elif b>a and b>c:
        print(f'{b} is the largest')
else:
    print(f'{c} is the largest')



#count odd and even numbers of the digits entered
even=[]
odd=[]
number=(input('Enter a number: '))
for i in number:
    if int(i)%2 ==0:
        even.append(int(i))
    else:
        odd.append(int(i))
print(even)
print(odd)

