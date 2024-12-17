# dictionary: "key":value inshort word is a key and its meaning is its value
# dicts are unordered,mutable and they do not duplicate keys
info = {
    "name": "morpheus",
    "subjects": ["Linear Algebra","C","Calculus"],
    "fav_mc's" :("k-dot","jcole","nas","pac"),
    "fav_hobby":"reading",
    "age" : 19,
    "can_vote" :True
}
print(type(info))
print(info["fav_mc's"]) #this is how you can access any value from dict
# this is will give you an error since it doesnot exist in the dict
print(info["fav_food"])
info["name"] = "luard"
print(info["name"])

# empty dict
null_dict = {}
null_dict["name"] = "john"
print(null_dict["name"])

# nested dictionaries
student = {
    "name" : "jia",
    "subjects" : {
        "calculus" : "A",
        "linear algebra" : "B",
        "chem" : "A"
    }
}
print(student["name"])
print(student["subjects"])
print(student["subjects"]["calculus"])

# dictionary methods
print(student.keys()) #nested keys wont be present in the output 
print(list(student.keys())) #to convert the dict into a list
print(tuple(student.keys())) #to convert the dict into a tuple
print(len(student)) #to find out the total number of keys in the dict
print(student.values()) #returns the values from the dict
print(student.items()) #returns a key-value pair
print(student.get("name")) #its another way of accessing key and it will return none for non existing key
student.update({"games": "valorant"})
print(student)

# since dictionary doesnt allow duplicate keys it always overwrites the value of an existing key whenever you are trying to add a new value to the same old key

# Set is a collection of unordered items, every item should be unique and immutable. lists and dict cannot be stored in a set since they are mutable. set is mutable since new elements can be added to it but its elements should always be immutable and hashable
# set basically ignores duplicate elements and stores it only once

nums = {1,2,3,4,"hello",32.34}
print(type(nums))

# empty set
collection = set()
print(type(collection))

# Set Methods
collection.add(23)
collection.add("helloworld")
collection.add(23.32)
print(collection)
collection.add(2)
collection.remove(23)
collection.add((3,4,5,6))
collection.pop()
collection.clear() #to clear the set
print(collection)

set1 = {1,2,3,4}
set2 = {3,5,63,2}
print(set1.union(set2)) #{1,2,3,4,5,63}
print(set1.intersection(set2)) #{2,3}

# store the meaning of the following words in a python dictionary "table": "a piece of furniture","list of facts and figures", "cat": "a small animal"

dict = {
    "table": ["a piece of furniture","list of facts and figures"],
    "cat": "a small animal"
}
print(dict)

# you are given a list of subjects for students. Assume one classroom is required for 1 subject. how many classrooms are needed by all students "python","java", "c++", "python","js","java","c++","c"

subjects = {"python","java", "c++", "python","js","java","c++","c"}
print(len(subjects))

# wap to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary and add one by one. use subject name as key and marks as value

academics = {}
x = int(input("enter marks of phy:" ))
academics.update({"phy":x})
x = int(input("enter marks of chem:" ))
academics.update({"chem":x})
x = int(input("enter marks of maths:" ))
academics.update({"maths":x})
print(academics)

#figure out a way to store 9 and 9.0 as separate values in the set

# store 9.0 as string
values = {9,"9.0"}
print(values) 

# use a tuple
value1 ={
    ("float", 9.0),
    ("int", 9)
}
print(value1)