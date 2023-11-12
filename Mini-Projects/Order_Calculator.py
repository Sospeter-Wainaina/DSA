# TODO
def order_burger():
    size = input("What Burger size would you like to order ? ")
    add_mushroom = input("Do you want to add mushroom ? ")
    extra_cheese = input("Do you want cheese? ")
    if size == 'M':
        price = 5
    elif size == 'N':
        price=8
    else :
        price = 10
    if add_mushroom == 'Y':
        mush_size = input("What size do you like your mushroom? ")
        if mush_size=='Mini' or mush_size=='Normal':
            price += 1
        else:
            price += 2
    if extra_cheese=='Y':
        price+=1
    return price

print(order_burger())