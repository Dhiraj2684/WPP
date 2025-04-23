n = int(input("Enter the number of items: "))
print("Enter name and price respectively!!")
products = {}
for i in range(n):
    names = input()
    prices = float(input())
    products[names] = prices
#print(products)
print("Type end to exit!!")
while True:
    query = input("Enter product name: ")
    if query == "end":
        break
    else:
        if query in products:
            print(f"{query} -> {products[query]}")
        else:
            print("Product not found")