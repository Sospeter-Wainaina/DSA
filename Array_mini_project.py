# Users input

def highest_temp(p_list, avg):
    for i, v in enumerate(p_list):
        if v > avg:
            if i == 0:
                print(
                    f"The {i}st Day was Higher than the Total temperature with {v} ")
            elif i == 1:
                print(
                    f"The {i}nd Day was Higher than the Total temperature with {v} ")
            elif i == 2:
                print(
                    f"The {i}rd Day was Higher than the Total temperature with {v} ")
            else:
                print(
                    f"The {i}th Day was Higher than the Total temperature with {v} ")


inp = int(input("How many days do you want to calculate AVG for? : "))
count = 1
my_temp = list()
while inp >= count:
    if count == 1:
        temp = int(input(f"What is the {count}st Day Highest Temp? :"))
    elif count == 2:
        temp = int(input(f"What is the {count}nd Day Highest Temp? :"))
    elif count == 3:
        temp = int(input(f"What is the {count}rd Day Highest Temp? :"))
    else:
        temp = int(input(f"What is the {count}th Day Highest Temp? :"))
    my_temp.append(temp)
    count += 1
avg = sum(my_temp)/len(my_temp)
highest_temp(my_temp, avg)
