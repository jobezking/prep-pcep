# Lists (mutable) 
fruits = ["apple", "pear", "orange", "banana"]
Apple = fruits[0]
fruits.append("grape")
_a = list(["apple", "pear", "orange", "banana"]) # using list() constructor
last_a = _a[-1] #access last item in list
#slicing below. slicing is list[x:y]
#x is position in the list. y is position in the list minus 1. If x is omitted i.e. [:4] it will default to 0
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a_slice = a[1:4]  # will contain [2, 3, 4]
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a_slice = a[1:4]  # will contain [1, 2, 3]
#advanced slicing uses interval: list[x:y:z] where z is interval
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8] 
every_other_number = numbers[0:9:2] #every_other_number = [0,2,4,8]
numbers_slice_length = len(numbers) + 1
print(numbers[0:numbers_slice_length:2])

#delete operations
a.pop()     #deletes last item
a.remove(2) #deletes value 2 in list (not position) i.e. fruits.remove("pear")
del a[2]    #deletes third item
del a       #deletes list
a.clear()   #empties list but retains reference

# Tuples (immutable)
days = ('Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
weekend = days[5:8] #slicing works the same as with lists, returns Friday, Saturday

# Dictionaries. key:value pairs. Values: of any data type and mutable. Keys: unique and immutable
d = {1: 'This', 2: 'Program', 3: 'Is', 4: 'Python', 5: 9, 'Python': 4}
d_empty = {}            #create empty list
d2 = dict(a = "Test", b = "for", c = "Courage")  # create using dict() constructor
language = d[4]                 #access value using key
language_number = d['Python']   #access value using key
d[4] = 'Java'                   #change value using key
d_empty["first"] = fruits[1]    #add data to dictionary by specifying new key ("first") and new value (fruits[1])
del d2['b']                     #drop key value pair by key
d3 = dict(key1=fruits, key2 = "coffee mug", key3 = 9) # create dictionary that contains list