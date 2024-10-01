duck_amount = int(input("duck amount: "))
duck_quality = (150,250,500,1000,2500,5000)
duck_unit_prices = (2.95,2.67,2.37,2.07,1.88,1.71,1.51)
item_index = 0
for quality in duck_quality:
    if duck_amount <= quality:
        break
    item_index += 1
duck_unit_price = duck_unit_prices[item_index]
print(f"price is {duck_unit_price} for {duck_amount} ducks")