
#my_list=['1','2','3','4','5','6','7','8','9','10']
# my_file = open('./docs/Countries.txt','w')


with open('./docs/Countries.txt','r') as file:
    print(file.readlines()[:])
        #print(file.readline())
# 'r' - read used when you want to read the file
# 'w' - write used when you want to overwrite the file
# 'a' - append used when you want to add something to the end of the file
# 'r+' - read and write used when you want to read and write to the file
# 'w+' - write and read used when you want to overwrite the file
# 'a+' - append and read used when you want to add something to the end of the file
# 'rb' - read binary  used for images
# 'wb' - write binary used for images
# 'ab' - append binary used for images