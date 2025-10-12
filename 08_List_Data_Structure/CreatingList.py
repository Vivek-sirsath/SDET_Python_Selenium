from itertools import count

empty_list = []

print(empty_list)  # []
print(type(empty_list))  # <class 'list'>

list_1 = ["Madhavi", "London", 25000.15, 9425467527, 25000.15]
print(list_1)  # ['Madhavi', 'London', 25000.15, 9425467527, 25000.15] - Insertion Order Preserved

# # eval() function -  Evaluates the data type
# print(input("Enter data:"))  # 10
# var1 = eval(input("Enter data:"))
# print(type(var1))   # <class 'int'>

# 10 --> <class 'int'>
# 10, "Ishita", 50000.12, 26 --> <class 'tuple'>
# [10, 'ishita', 50000, 26] --> <class 'list'>

# range() function has range data type
print(range(11))   # range(0, 11)
print(type(range(11)))  # <class 'range'>
# convert range data type to list data type.
print(list(range(11)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Access elements inside the list
# 1) By Index
# 2) By Slice Operator

#               0          1         2         3           4
# list_1 = ["Madhavi", "London", 25000.15, 9425467527, 25000.15]
#              -5         -4        -3        -2          -1

# 1) Index
print("================ By Index ================")
print(list_1[1])  # London   -->  Forward direction
print(list_1[-2])  # 9425467527
print(list_1[-4])  # London  <--  Backward direction
# print(list_1[-10])  # IndexError: list index out of range

print("================ By Slice Operator ================")
# 2) Slice Operator - list[start:end:step]

# step +ve if moving in forward direction
# step -ve if moving in backward direction

#               0          1         2         3           4
# list_1 = ["Madhavi", "London", 25000.15, 9425467527, 38500.75]
#              -5         -4        -3        -2          -1

print(list_1[1:3])  # ['London', 25000.15]
print(list_1[0:4])  # ['Madhavi', 'London', 25000.15, 9425467527]
print(list_1[2:2])  # []
print(list_1[-1:-4:-1])  # [25000.15, 9425467527, 25000.15]

list_2 = [111,222,333,444,555,666,777,888,999]
print(list_2[-1:-7:-1])  # [999, 888, 777, 666, 555, 444]

# List is mutable data structure
# We can modify the existing list using index.
list_2[2] = "Apple"
print(list_2)  # [111, 222, 'Apple', 444, 555, 666, 777, 888, 999]
list_2[-6] = 9999
print(list_2)  # [111, 222, 'Apple', 9999, 555, 666, 777, 888, 999]

# ========= TRAVERSING - SEQUENTIAL ACCESS OF ALL THE ELEMENTS INSIDE THE LIST =========

# Print all elements using for loop
for x in list_1:
    print(x)

#============== Functions to be applied on list ==============#

sample_list = [10,20,30,40,50,20]

# 1) len() - returns length
print("Length of list: ", len(sample_list))  # Length of list:  6

# 2) count() - returns how many times the object is repeated?
print(sample_list.count(20))  # 2

# 3) index() - returns index of first occurrence of specified item.
print("index of 40 is:- ", sample_list.index(40))  # 3

## If the specified item not present in the list,  will throw 'ValueError'.
# print("index of 70 is:- ", sample_list.index(70))  # ValueError: 70 is not in list

# 4) append() - to add an item at the END of the list
sample_list.append("Madhavi")
print(sample_list)   # [10, 20, 30, 40, 50, 20, 'Madhavi']

# 5) insert() - wil add an item at the specific index
sample_list.insert(2,"XX")
print(sample_list)   # [10, 20, 'XX', 30, 40, 50, 20, 'Madhavi']

## If the (specified index > max index), item will be inserted at the END position of the list
sample_list.insert(10, 3)
print(sample_list) # [10, 20, 'XX', 30, 40, 50, 20, 'Madhavi', 3]

## If the (specified index < min index), item will be inserted at the START position of the list
sample_list.insert(-12, 'Blue')
print(sample_list)  # ['Blue', 10, 20, 'XX', 30, 40, 50, 20, 'Madhavi', 3]

# 6) extend() - this function adds one list to another list
additional_list = [1000,2000,3000]
sample_list.extend(additional_list)
print("extended list -", sample_list)  # ['Blue', 10, 20, 'XX', 30, 40, 50, 20, 'Madhavi', 3, 1000, 2000, 3000]

# 7) remove() - use to remove specified items from the list.
# If item is present multiple times, then only first occurrence will be removed.
sample_list.remove(2000)
print(sample_list)  # ['Blue', 10, 20, 'XX', 30, 40, 50, 20, 'Madhavi', 3, 1000, 3000]

## If the specified item is repeated multiple times, then only first occurrence will be removed.

## If the specified item not present in the list,  will throw 'ValueError'
# sample_list.remove(90)
# print(sample_list)  # ValueError: list.remove(x): x not in list

# 8) pop() - It removes and returns the last element of the list if index is not specified.
sample_list.pop()
# last '3000' will be removed
print(sample_list)  # ['Blue', 10, 20, 'XX', 30, 40, 50, 20, 'Madhavi', 3, 1000]

## If the specified index is out of list or if the list is empty, will throw 'IndexError'
# sample_list.pop(11)
# print(sample_list)  # IndexError: pop index out of range

# 9) reverse() - Use to reverse the order of the elements of  the list
sample_list.reverse()
print(sample_list)  # [1000, 3, 'Madhavi', 20, 50, 40, 30, 'XX', 20, 10, 'Blue']

# 10) sort()
# In list, insertion order is preserved by default.
# If we want to sort,  still we can sort by using 'sort()' method.
## For numbers => default sorting order is Ascending Order
## Eor String => default sorting order is Alphabetical Order

number_list = [40,10,80,20,50,30]
number_list.sort()
print(number_list)  # [10, 20, 30, 40, 50, 80]

string_list = ["Zebra", "Elephant", "Cat", "Jaguar", "Dog", "Lion"]
string_list.sort()
print(string_list)  # ['Cat', 'Dog', 'Elephant', 'Jaguar', 'Lion', 'Zebra']

# 11) clear() - To remove all the elements from the list
sample_list.clear()
print(sample_list)  # [] - Empty List

# 12) max() - returns the max value
print("max() -", max(number_list))  # 80

# 13) min() - returns the min value
print("min() -", min(number_list))  # 10

print("=================== REMOVING MULTIPLE ITEMS FROM THE LIST ===================")

number_list = [40,10,80,20,100,50,30,70,130,80,40,90,120,]
print("Before - ", number_list)
print("Remove - 80, 120,130,70,40")
# If duplicate elements are present, it will remove the first occurrence.
items_to_remove = [80,120,130,70,40]

for item in items_to_remove:
    if item in number_list:
        number_list.remove(item)

print("After - ", number_list)  # [10, 20, 100, 50, 30, 80, 40, 90]








