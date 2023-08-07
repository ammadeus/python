#1. Write a decorator that ensures a function is only called by users with a specific role. Each function should have an user_type with a string type in kwargs. 

def is_admin(user_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user_type == 'admin':
                return func(*args, **kwargs)
            else:
                raise PermissionError("Access denied")
        return wrapper
    return decorator

@is_admin(user_type='admin')
def show_customer_receipt():
    pass

show_customer_receipt()


#2. Write a decorator that wraps a function in a try-except block and prints an error if any type of error has happened.

def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Error is:", e)
    return wrapper

@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])

some_function_with_risky_operation({'foo': 'bar'})


#3. Optional: Create a decorator that will check types. It should take a function with arguments and validate inputs with annotations.
# It should work for all possible functions. Don`t forget to check the return type as well

def check_types(func):
    def wrapper(*args, **kwargs):
        for arg, (param_name, param_type) in zip(args, func.__annotations__.items()):
            if not isinstance(arg, param_type):
                raise TypeError(f"Argument '{param_name}' must be {param_type.__name__}, not {type(arg).__name__}")

        
        result = func(*args, **kwargs)
        
        return_type = func.__annotations__.get('return')
        if return_type is not None and not isinstance(result, return_type):
            raise TypeError(f"Return type a must be {return_type.__name__}, not {type(result).__name__}")
        
        return result

    return wrapper




@check_types
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)
#3

add("1", "2")
#TypeError: Argument a must be int, not str