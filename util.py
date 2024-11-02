"""Module utlities"""

def get_input(messge, return_type):
    """to get input from user"""
    while True:
        try:
            match return_type:
                case "int":
                    return int(input(messge))
                case "float":
                    return float(input(messge))
                case _:
                    input(messge)
        except Exception as exp:
            print(exp)
