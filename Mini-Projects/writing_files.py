#To write to a file, you must add a second argument to the open() function, "w" to write.
# you can use with open() as file: to open a file and close it automatically
with open('docs/Countries.txt','w') as file: # 'w' - write used when you want to overwrite the file
    file.write('Kenya\n')

# To append to a file, you must add a second argument to the open() function, "a" to append.
with open('docs/Countries.txt','a') as file: # 'a' - append used when you want to add to the file
    file.write('Tanzania\n')

#Now when we read we get the following output [Kenya, Tanzania]
with open('./docs/Countries.txt','r') as file:
    print(file.read()) #readlines() - returns a list of all the lines in the file