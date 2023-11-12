degree = int(input("Input the Degrees in Celsius/Fahrenheit that you want to Convert : "))

def conversion_engine(degrees):
    '''It takes one parameter and converts it to Fahrenheit or Celsius'''
    #find out if they want to convert from Celsius to Fahrenheit or opposite
    converTo = input("What do you want to covert to ?")
    if converTo == 'Fahrenheit':
        converted = (degrees*1.8 + 32)
    else:
        converted = (degrees-32)/1.8
    return f"Your converted rate in {type} is {converted}"

print(conversion_engine(degree))