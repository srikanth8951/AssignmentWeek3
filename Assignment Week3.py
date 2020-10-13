# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 22:09:52 2020

@author: hvsri
"""

"""
Question1:
    a: Write a function that prints out the odd numbers 1 through 99. Bonus: Use list comprehension.

"""
def oddNumber():
    oddnum = [num for num in range(1, 100) if num % 2 == 1] 
    print(oddnum)
    
oddNumber()

"""############################"""

"""
Question1:
    b: Write a function that takes in a dictionary and outputs the most frequent value in the dictionary.
    
"""
dictInput = {'aa': 2, 'bb': 2,
    'cc': 1, 'dd': 4, 'ee': 2,
    'ff': 1, 'gg': 6,}


temp={}

for key,value in dictInput.items():
    if value not in temp:
        temp[value]=0
    else:
        temp[value]+=1

print(max(temp,key=temp.get))

"""############################"""

"""
Question1:
    c: Write a function to reverse a string. The string can be of any length and might be empty. Bonus: Implement recursively

"""
def reverse(str1):
    print(str1)
    if len(str1) == 0:
        return str1
    else:
        return reverse(str1[1:]) + str1[0] 


str1 = input("Enter the string to be reversed: ")

print("The Given String  is: ", str1)

print("Reversed String is: ", reverse(str1))

"""############################"""

"""
Question1:
    d: Write a function that takes in two sorted lists and merges them (don’t use any Python built in functions or methods, such as the list.sort method). 
    So the input ([1, 5, 8], [4, 7, 10, 12]) should yield the output [1, 4, 5, 7, 8, 10, 12]. 
    The lists may not be of the same length, and one or both may be empty.

"""
def meargeList(list1, list2): 
    print ("The original list 1 is : " + str(list1)) 
    print ("The original list 2 is : " + str(list2))
    
     
    size_1 = len(list1) 
    size_2 = len(list2) 
    
    res = [] 
    i, j = 0, 0
    
    while (i < size_1 and j < size_2): 
    	if (list1[i] < list2[j]): 
    		res.append(list1[i]) 
    		i += 1
    
    	else: 
    		res.append(list2[j]) 
    		j += 1
    
    res = res + list1[i:] + list2[j:]  
    print ("The combined sorted list is : " + str(res)) 

list1 = [1, 5, 8]
list2 = [4, 7, 10, 12] 
meargeList(list1, list2)

"""############################"""

"""
Question 2: A clerk works in a store where the cost of each item is a positive integer number of dollars

"""

def pay_change(paid, cost):
   
    change = paid - cost
    result = {}


    n_twenty = change // 20
    result['$20'] = n_twenty
    rest = change % 20

    n_ten = rest // 10
    result['$10'] = n_ten
    rest = rest % 10

    n_five = rest // 5
    result['$5'] = n_five
    rest = rest % 5

    n_two = rest // 2
    result['$2'] = n_two
    rest = rest % 2

    n_one = rest // 1
    result['$1'] = n_one

 
    for k, v in result.items():
        if v != 0:
            print('Need', v, 'bills of', k)

paid = int(input('Enter the amount paid: '))
cost = int(input('Enter the cost of item: '))            
pay_change(paid, cost)


"""############################"""

"""
Question 3:

(a) Write a procedure that takes a string of words separated by spaces (assume no punctuation or capitaliza-tion), together with a "target" word, and shows the position of the target word in the string of words.

"""

def procedure(string,target):
    words=string.split(" ") 
    solution=[] 
    for i in range(len(words)):
        if words[i]==target: 
            solution.append(i)
    if len(solution)==0: 
        return False
    return solution

string="we dont need no education we dont need no thought control no we dont"
print (procedure(string, "dont"))

"""############################"""


"""
Question 4: One classic method for composing secret messages is called a square code. 
            The spaces and punctuation are removed from the english text and the characters are written into a square (or rectangle). 

"""


def get_matrix(text, c=1, r=1):
    if c * r >= len(text):
        return (c, r)

    if not (c >= r and c - r < 1):
        r += 1
    else:
        c += 1
    return get_matrix(text, c, r)
    

def encode(plain_text):
    normalized_text = ''.join(c.lower() for c in plain_text if c.isalnum())
    
    if not normalized_text:
        return ''

    columns, rows = get_matrix(normalized_text)
    
    chunks = [normalized_text[i * columns: i * columns + rows + 1] for i in range(0, rows + 1)]

    partials = [[] for _ in range(rows + 1)]
    
    for chunk in chunks:
        for i in range(columns):
            if i < len(chunk):
                partials[i].append(chunk[i])
    
    final = [''.join(p) for p in partials if p]
    
    result = ' '.join(final)
    
    expected_length = (columns * rows) + (rows - 1)
    if len(result) < expected_length: 
        result += ' ' * (expected_length - len(result))
    return result

plain_text = input('Enter the text: ')

print(encode(plain_text))


"""############################ END #################"""



