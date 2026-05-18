from product import Product
from inventory_manager import add_product, view_products


def search_product():
    product_id = input("Enter Product ID: ")

    try:
        with open("products.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if data[0] == product_id:
                    print("Product Found:", line.strip())
                    return

        print("Product not found")

    except FileNotFoundError:
        print("Inventory file not found")


while True:
    print("\nINVENTORY MANAGEMENT SYSTEM")
    print("1 Add Product")
    print("2 View Products")
    print("3 Search Product")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            quantity = int(input("Enter Quantity: "))

            product = Product(product_id, name, price, quantity)

            add_product(product)

            print("Product added successfully")

        except ValueError:
            print("Invalid input")

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        print("Program exited")
        break

    else:
        print("Invalid option")
        #mgm