# 1
def triple(value):
    return 3*value
def tripleStuff(a_list):
    new_seq = map(triple,a_list)
    return list(new_seq)
def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2,5,9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)

#Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst.
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

greeting_doubled = list(map(lambda item: 2*item, lst))
print(greeting_doubled)

# Below, we have provided a list of strings called abbrevs. Use map to produce a new list called abbrevs_upper that contains all the same strings in upper case.
abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
abbrevs_upper = list(map(lambda st: st.upper(), abbrevs))
print(abbrevs_upper)

# 2
def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(keep_evens([3,4,6,7,0,1]))

# Write code to assign to the variable filter_testing all the elements in lst_check that have a w in them using filter.
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
filter_testing = list(filter(lambda word: "w" in word, lst_check))
print(filter_testing)

# Using filter, filter lst so that it only contains words containing the letter “o”. Assign to variable lst2. Do not hardcode this.
lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
lst2 = list(filter(lambda word: "o" in word, lst))
print(lst2)

# 3
things = [2,5,9]
yourlist = [value*2 for value in things]
print(yourlist)

def keep_evens(nums):
    new_list = [num for num in nums if num%2 == 0]
    return new_list
print(keep_evens([3,4,6,7,0,1]))

# 4
things2 = [3,4,6,7,0,1]
print(list(map(lambda x: x*2, filter(lambda y: y%2 == 0, things2))))

#equivalent
print([x*2 for x in things if x%2 == 0])

# The for loop below produces a list of numbers greater than 10. Below the given code, use list comprehension to accomplish the same thing. Assign it the the variable lst2. Only one line of code is needed.
L = [12, 34, 21, 4, 6, 9, 42]
lst2 = [value for value in L if value>10]
print(lst2)

#  Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the dictionary tester. Do this using a list comprehension.
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
new = tester['info']
#import json
#print(json.dumps(tester['info'],indent = 2))
compri = [d['name'] for d in new]
print(compri)

# 5
L1 = [3,4,5]
L2 = [1,2,3]
L4 = list(zip(L1,L2))
L3 = []

for (x1, x2) in L4:
    L3.append(x1+x2)
#print(L3)

# List comprehension
L5 = [x1+x2 for (x1,x2) in L4]
print(L5)
# Map
L6 = list(map(lambda x: x[0]+x[1], L4))
print(L6)

# Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension,
# create a new list, L3, that sums the two numbers if the number from L1 is greater than 10
# and the number from L2 is less than 5. This can be accomplished in one line of code.
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
L3 = [x1+x2 for (x1,x2) in list(zip(L1,L2)) if x1>10 and x2<5]
print(L3)

# 6
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for i in range(len(word)):
        bc = blanked[i]
        wc = word[i]
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
     #for (bc, wc) in zip(blanked, word):
      #  if bc == '_' and wc in guesses_made:
      #      return False
      #  elif bc != '_' and bc != wc:
      #      return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))

