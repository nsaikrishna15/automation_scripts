sentence1 = input("Enter your first sentance: ")
sentence2 = input("Enter your second sentance: ")

list1 = sentence1.split()
list2 = sentence2.split()

list3 = set(list1)&set(list2)

list4 = sorted(list3, key = lambda k : list1.index(k))

print(list4) # Prints Common Words

# print(set(list1) - set(list2)) # Prints words that are in sentence 1 but not in sentence 2
#
# print(set(list2) - set(list1)) # Prints words that are in sentence 2 but not in sentence 1