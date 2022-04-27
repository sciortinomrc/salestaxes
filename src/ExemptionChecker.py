class ExemptionChecker:
    def __init__(self):
        self.__exempt_products = [
            "book",
            "chocolate",
            "pills"
        ]

    def is_product_tax_exempt(self, product):
        for entry in self.__exempt_products:
            if entry in product:
                return True

        return False