from ExemptionChecker import ExemptionChecker
exemption_checker = ExemptionChecker()

class TaxApplicator:
    def apply_basic_tax(self, name, price):
        if exemption_checker.is_product_tax_exempt(name):
            return 0
        
        return (price * 10 / 100)

    def apply_import_tax(self, price, imported):
        if not imported:
            return 0
        return (price * 5 / 100)

    def round_up_price(self, price):
        return round(price * 100) / 100

    def apply_tax(self, name, price, imported):
        basic_taxed_price = self.apply_basic_tax(name, price)
        import_taxed_price = self.apply_import_tax(price, imported)
        return self.round_up_price(price + basic_taxed_price + import_taxed_price)

