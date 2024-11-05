"""Module utlities"""

def get_input(messge:str, return_type:str):
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
                    return int(input(messge))
                case "float":
                    return float(input(messge))
                case _:
                    return input(messge)
        except Exception as exp:
            print(exp)
