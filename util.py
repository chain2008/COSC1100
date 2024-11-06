"""Module utlities"""

def get_input(messge:str, return_type:str, validate = None):
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
                    ret = int(input(messge))
                case "float":
                    ret = float(input(messge))
                case _:
                    ret = input(messge)
            if validate != None and validate(ret) == False:
                raise ValueError("error validation")
            return ret
        except Exception as exp:
            print(exp)
