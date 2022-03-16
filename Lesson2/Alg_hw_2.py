# Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

og_str="geeksforgeeks"

first_half=og_str[:(len(og_str)//2)]
second_half=og_str[len(og_str)//2:]
new_str=second_half+first_half

print(first_half)
print(second_half)
print(new_str) #not sure how to handle the extra charachter if it is odd




####################################
# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.
# Hint:

def unique(string:str):
    string=string.lower()
    d= {}
    for l in string:
            if l not in d:
                d[l] = 1
            else:
                d[l] +=1

    for k, v in d.items():
        if v <=1:
            return True
        else:
            return False

print(unique('abcdefghijkl'))
print(unique('aabcdea'))