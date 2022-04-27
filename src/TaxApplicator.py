from ExemptionChecker import ExemptionChecker
import math
exemption_checker = ExemptionChecker()

class TaxApplicator:
    def apply_basic_tax(self, name, price):
        if exemption_checker.is_product_tax_exempt(name):
            return price
        
        price = price + (price * 10 / 100)

        price = math.ceil(price * 1000) / 1000
        return price

    def apply_import_tax(self, price, imported):
        if not imported:
            return price
        price = price + (price * 5 / 100)

        price = math.ceil(price * 1000) / 1000
        return price

