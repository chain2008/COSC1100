"""Module utlities"""

def get_input(message:str, return_type:str):
    """
    https://peps.python.org/pep-0257/

    to get input from user.

    Keyword arguments:
    message(str) -- message shown on user input. 
    return_type(str) -- "int" | "float".
    """
    while True:
        try:
            match return_type:
                case "int":
                    ret = int(input(message))
                case "float":
                    ret = float(input(message))
                case _:
                    ret = input(message)
            return ret
        except Exception as exp:
            print(exp)

def get_input(message:str, return_type:str, validate:callable):
    """
    https://peps.python.org/pep-0257/

    to get input from user.

    Keyword arguments:
    message(str) -- message shown on user input. 
    return_type(str) -- "int" | "float".
    validate -- validation function.
    """
    while True:
        try:
            ret = get_input(message, return_type)
            if validate(ret) == False:
                raise ValueError("error validation")
            return ret
        except Exception as exp:
            print(exp)
