import array as arr

# you need to specify a typecode for every type of array, for ex: i for integers, f for float etc

value = arr.array('i', [5,4,3,2,1])
# print(value)

# buffer_info() returns the address of the array and the count of the elements present in the array
# print(value.buffer_info())

# append() adds value at the end
value.append(6)
# print(value)

# remove()
value.remove(4)
# print(value)

# pop() : it removes the last value from the array
value.pop()
# print(value)

#reverse()
value.reverse()
# print(value)

# printing elements of array
# for i in range(4):
    # print(value[i])

# if you dont know the length of the array
# for i in range(len(value)):
    # print(value[i]) 

# to create a new array using an existing array
# the elements currently in value array are 1,2,3,5 
newArr = arr.array(value.typecode,(a for a in value))

# for a in range(len(newArr)):
    # print(newArr[a])

# using while loop 
# i = 0
# while(i<len(newArr)):
# print(newArr[i])
# i+=1 

# taking input from the user
# my_arr = arr.array('i',[])
# n = int(input("enter the length of the array: "))
# for i in range(n):
#     x = int(input("enter the elements of the array: "))
#     my_arr.append(x)
# print(my_arr)
















# sum of elements in an array
# def sum_of_array(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum = sum + arr[i]
#     return sum
# print(sum_of_array([1,2,3,4,5]))

# find max and min elements from the arr
# def max_min_array(arr):
#     # max_val = max(arr)
#     # min_val = min(arr)
#     max_val = arr[0]
#     min_val = arr[0]
#     for i in range(len(arr)):
#         if arr[i] > max_val:
#             max_val = arr[i]
#         else:
#             min_val = arr[i]
#     return (max_val,min_val)
# print(max_min_array([1,2,3,4,5]))

# count occurences of a particular value
# def count_occurences(arr):
#     count = 0
#     for i in range(len(arr)):
#         if (arr[i] == 1):
#             count += 1
#     return count
# optimize way of doing the same thing
# def count_occurences(arr,target=1):
#     return arr.count(target)
# print(count_occurences([5,3,4,2,1,1,6]))


# reverse an array
# def reverse_array(arr):
#     # return arr[::-1]
#     # doing the same thing without using slicing
#     for i in range(len(arr)//2):
#         temp = arr[i]  # Save the current element
#         arr[i] = arr[len(arr) - i - 1]  # Assign the corresponding element from the end
#         arr[len(arr) - i - 1] = temp  # Place the saved element at the end
#     return arr  
# print(reverse_array([1,2,3,4,5]))

# remove even numbers
# the optimized way to do it would just check for odd numbers,append them in an array and return the array
# def remove_even_num(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         if (arr[i] % 2 == 0):
#             continue
#         else:
#             new_arr.append(arr[i])
#     return new_arr
# print(remove_even_num([2,3,4,5,6]))


# rotate an array
# def rotate_array(arr,n):
#     for i in range(len(arr)):
#         if( n > 0):
#             n = len(arr) + n
#         else:
#             n = len(arr) + n
#     return n
# print(rotate_array([1,2,3,4,5],2))
