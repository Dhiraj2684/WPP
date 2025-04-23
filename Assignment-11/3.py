import pandas as pd
asking_price_input = input("Enter asking price (comma-separated): ")
fair_price_input = input("Enter fair price (comma-separated): ")

asking_price_list = asking_price_input.split(',')
fair_price_list   = fair_price_input.split(',')

asking_price = pd.Series(asking_price_list)
fair_price   = pd.Series(fair_price_list)

good_deal_index = []

if len(asking_price) != len(fair_price):
    print("Error: The number of asking price and fair price must be the same.")
else:
    for i in range(len(asking_price)):
        if(asking_price[i] < fair_price[i]):
            good_deal_index.append(i)
    print("Good deal indices:", good_deal_index)