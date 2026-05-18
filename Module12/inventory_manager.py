def add_product(product):
    with open("products.txt", "a") as file:
        file.write(product.get_product_info() + "\n")


def view_products():
    try:
        with open("products.txt", "r") as file:
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("No products found.")
        #mgm