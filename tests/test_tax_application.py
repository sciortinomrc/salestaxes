import logging
from Product import Product
from TaxApplicator import TaxApplicator
log = logging.getLogger("test.tax_application")

def test_apply_tax_to_exempt_product():
    input = "1 book at 12.49"
    product = Product(input)
    product.process()

    tax_applicator = TaxApplicator()
    product.taxed_price = tax_applicator.apply_basic_tax(product.name, product.price)

    assert product.taxed_price == 12.49

def test_apply_tax_to_product():
    input = "1 bottle of perfume at 18.99"
    product = Product(input)
    product.process()

    tax_applicator = TaxApplicator()
    product.taxed_price = tax_applicator.apply_basic_tax(product.name, product.price)

    assert product.taxed_price == 20.889

def test_apply_import_tax_to_product():
    input = "1 imported bottle of perfume at 27.99"
    product = Product(input)
    product.process()

    tax_applicator = TaxApplicator()
    product.taxed_price = tax_applicator.apply_basic_tax(product.name, product.price)

    assert product.taxed_price == 30.789

