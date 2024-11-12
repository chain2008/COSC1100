"""Module utlities"""

def get_input(messge:str, return_type:str = None, validate:callable = None):
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
            match return_type:
                case "int":
                    ret = int(input(messge))
                case "float":
                    ret = float(input(messge))
                case _:
                    ret = input(messge)
            if validate is not None and validate(ret) is False:
                raise ValueError("error input")
            return ret
        except Exception as exp:
            print(exp)
