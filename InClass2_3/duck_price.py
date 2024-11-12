DUCK_PRICES = {
    150: 2.95,
    250: 2.67,
    500: 2.37,
    1000: 2.07,
    2500: 1.88,
    5000: 1.71,
    float('inf'): 1.51
}

def get_price(duck_amount):
    """Function get duck unit price"""
    for item in DUCK_PRICES.items():
        if duck_amount <= item[0]:
            return item[1]
    raise ValueError("Unknown Error")
