# Decorators are used to modify the functionality of function or class without changing the original code.
# They take in a function as a parameter does something to it and then returns it.

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print(f'Wrapper function executed before {original_function.__name__} function')
        return original_function(*args,**kwargs)
    return wrapper_function

def my_logger(original_function):
    import logging
    logging.basicConfig(filename=f'{original_function.__name__}.log',level=logging.INFO)
    def wrapper_function(*args,**kwargs):
        logging_info = f'Ran with args: {args}, and kwargs: {kwargs}'
        logging.info(logging_info)
        return original_function(*args,**kwargs)
    return wrapper_function
# def display():
#     print('display function ran')
#
# decorated_display = decorator_function(display)
# decorated_display()
# why do we need to use decorators?
# say we want to add functionality to the display function without changing the original code.
# we can use decorators to do this.
# we can use the @ symbol to do this.

@decorator_function
def display():
    print('display function ran')

# we can see that the decorator function is executed before the display function.
@my_logger
def display_info(name,age):
    print(f'display_info ran with arguments ({name},{age})')

display_info('Sospeter',23)
# display()