from Database import Database
database = Database()
class Product:
    def __init__(self, input):
        self.__input = input
    
    def __detect_name(self):
        input_without_price = self.__input.split(" at ")[0].strip()
        input_without_price = input_without_price.split(" ")
        return " ".join(input_without_price)

    def __detect_price(self):
        raw_price = self.__input.split(" at ")[1]
        return float(raw_price)

    def __detect_imported(self):
        return "imported" in self.__input


    def process(self):
        name = self.__detect_name()
        product_info = database.get_item_info(name)
        price = self.__detect_price()
        imported = self.__detect_imported()

        self.name = name
        self.type = product_info["type"]
        self.category = product_info["category"]
        self.price = price
        self.imported = imported

    