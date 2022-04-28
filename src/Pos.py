from Product import  Product
from TaxApplicator import TaxApplicator

class Pos:
    def __init__(self):
        self.tax_applicator = TaxApplicator()
        self.basket = []

    def scan_item(self, item):
        product = Product(item)
        product.process()
        product.taxed_price = self.tax_applicator.apply_tax(product.name, product. price, product.imported)
        self.basket.append(product)

    def produce_bill(self):
        bill = []
        total = 0
        total_taxed = 0
        for product in self.basket:
            bill.append("%s: %.2f" % (product.name, product.taxed_price))
            total += product.taxed_price
            total_taxed += (product.taxed_price - product.price)
        bill.append("Sales Taxes: %.2f" % (self.tax_applicator.round_up_price(total_taxed)))
        bill.append("Total: %.2f" % (total))
        bill = "\n".join(bill)
        
        return bill

    def process_basket(self, input):
        basket = input.split("\n")
        for item in basket:
            self.scan_item(item) 

        return self.produce_bill()

