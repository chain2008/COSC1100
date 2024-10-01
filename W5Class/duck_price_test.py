duck_amount = int(input("duck amount: "))
if duck_amount <= 150:
    duck_unit_price = 2.95
elif duck_amount <= 250:
    duck_unit_price = 2.67
elif duck_amount <= 500:
    duck_unit_price = 2.37
elif duck_amount <= 1000:
    duck_unit_price = 2.07
elif duck_amount <= 2500:
    duck_unit_price = 1.88
elif duck_amount <= 5000:
    duck_unit_price = 1.71
else:
    duck_unit_price = 1.51
print(f"price is {duck_unit_price} for {duck_amount} ducks")