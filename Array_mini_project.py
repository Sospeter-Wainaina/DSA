def highest_temp(temp_list, avg):
    for i, temp in enumerate(temp_list):
        day = "st" if i == 0 else "nd" if i == 1 else "rd" if i == 2 else "th"
        print(
            f"The {i+1}{day} Day was Higher than the Average temperature with {temp}")


inp = int(input("How many days do you want to calculate AVG for? : "))
my_temp = []

for count in range(1, inp + 1):
    temp = int(input(
        f"What is the {count}{['st', 'nd', 'rd', 'th'][min(3, count - 1)]} Day Highest Temp? :"))
    my_temp.append(temp)

avg = sum(my_temp) / len(my_temp)
highest_temp(my_temp, avg)
