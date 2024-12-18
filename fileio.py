# text files: .txt, .docx, .log etc
# binary files: .mp4, .mov, .png, .mov, .jpeg

# r = open for reading
# w = open for writing and it removes the existing data from the file first before entering new data
# x = create a new file and open if for writing
# a = open for writing, appending to the end of the file if it exists
# b = binary mode
# t = text mode(default)
# + = open a disk file for updating(reading and writing)

f = open("hello.txt", "r")
# reads entire file
data = f.read()
# # readline() is use to read the content from the file one line at a time and if read() is used before calling readline() hence we dont see the output that is stored in line1
line1 = f.readline()
print(data, line1)
print(type(data))
f.close()
 
f = open("hello.txt", "w")
f.write("i wanna be the greatest!!!!")
f.close()

f = open("hello.txt", "a")
f.write("\ni remember you was conflicted")
f.close()

# r+ = you can read the file and overwrite existing data and the pointer is at the start
f = open("hello.txt", "r+")
f.write("kdot")
f.close()

# using with keyword

with open("hello.txt","r") as f:
    data = f.read()
    print(data)
# same for write mode and other modes

# for deleting a file
# use OS module
# import OS
# os.remove(filename or filepath)

# create a new file "practice.txt" using python. add the following data in it: hi everyone, it's nice to meet you. i love building stuff and listening to hiphop

f = open("practice.txt", "w")
f.write("hi everyone, it's nice to meet you. i love building stuff and listening to hiphop")
f.close()

# wap that finds hiphop 
word = "hiphop"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found") 


