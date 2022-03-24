# Reverse a Statement
# Build an algorithm that will print the given statement in reverse.
# Example: Initial string = Everything is hard before it is easy
# Reversed string = easy is it before hard is Everything
#
def wordReverse(str):
    i = len(str) - 1
    start = end = i + 1
    result = ''

    while i >= 0:
        if str[i] == ' ':
            start = i + 1
            while start != end:
                result += str[start]
                start += 1
            result += ' '
            end = i
        i -= 1
    start = 0
    while start != end:
        result += str[start]
        start += 1
    return result
print(wordReverse('Everything is hard before it is easy'))

#########################
#builtin functions
string = 'Everything is hard before it is easy'
split_str = string.split(' ') # split on spaces
reversed_str = reversed(split_str) # reverse words
final_str = ' '.join(reversed_str) # join the reversed words back to string
print("Reversed string: " , final_str)



# Permutations
# Write a solution that will print all permutations of a string.
# A permutation is an act of changing the arrangement of characters.
# Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}

def permute(s, answer):
    if (len(s) == 0):
        print(answer, end="  ")
        return

    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)


# Driver Code
answer = ""

s = input("Enter the string : ")

print("All possible strings are : ")
permute(s, answer)


# Count Characters
# Create a program that will count vowels and consonants in a string.
# Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}
print('\n')
str1 = input("Please Enter Your Own String : ")
vowels = 0
consonants = 0

for i in str1:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
            or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)