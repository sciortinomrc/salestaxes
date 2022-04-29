from ExemptionChecker import ExemptionChecker
import math 
exemption_checker = ExemptionChecker()

class TaxApplicator:
    def apply_basic_tax(self, name, price):
        if exemption_checker.is_product_tax_exempt(name):
            return 0
        
        return price * 10 / 100

    def apply_import_tax(self, price, imported):
        if not imported:
            return 0
        return price * 5 / 100

    def round_up_price(self, price):
        price = round(price, 3)
        pure = math.trunc(price*10)/10
        decimal = round(price - pure, 3) * 10
        if (decimal >= 0.25 and decimal <0.75):
            decimal = 0.5
        else:
            decimal = round(decimal, 1)
        decimal = round(decimal / 10, 2)
        return pure + decimal

    def apply_tax(self, name, price, imported):
        basic_taxed_price = self.apply_basic_tax(name, price)
        import_taxed_price = self.apply_import_tax(price, imported)
        taxes = self.round_up_price(basic_taxed_price + import_taxed_price)
        print(price, taxes, price+taxes, round(price + taxes, 2) )
        return round(price + taxes, 2)

