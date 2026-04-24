product = input("Enter product name: ")
price = input("Enter price: ")
with open("inventory.txt", "a") as file:
    file.write(product + "," + price + "\n")
print("Product saved successfully")
#MGM