class Product:

    def __init__(self, product_id, name, price, quantity):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_product_info(self):
        return f"{self.__product_id},{self.__name},{self.__price},{self.__quantity}"

    def get_id(self):
        return self.__product_id

    def update_quantity(self, quantity):
        self.__quantity = quantity
        #mgm