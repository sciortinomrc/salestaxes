import logging
from Product import Product
from TaxApplicator import TaxApplicator
log = logging.getLogger("test.tax_application")

def test_apply_tax_to_exempt_product():
    input = "1 book at 12.49"
    product = Product(input)
    product.process()

    tax_applicator = TaxApplicator()
    tax_value = tax_applicator.apply_basic_tax(product.name, product.price)

    assert tax_applicator.round_up_price(tax_value) == 0

def test_apply_tax_to_product():
    input = "1 bottle of perfume at 18.99"
    product = Product(input)
    product.process()

    tax_applicator = TaxApplicator()
    tax_value = tax_applicator.apply_basic_tax(product.name, product.price)

    assert tax_applicator.round_up_price(tax_value) == 1.9

def test_apply_import_tax_to_product():
    input = "1 imported bottle of perfume at 27.99"
    product = Product(input)
    product.process()

    tax_applicator = TaxApplicator()
    tax_value = tax_applicator.apply_basic_tax(product.name, product.price)

    assert tax_applicator.round_up_price(tax_value) == 2.8


def test_apply_all_taxes_exempt():
    input = "1 book at 12.49"
    product = Product(input)
    product.process()

    tax_applicator = TaxApplicator()
    tax_value = tax_applicator.apply_tax(product.name, product.price, product.imported)

    assert tax_applicator.round_up_price(tax_value) == 0

def test_apply_all_taxes_exempt_imported():
    input = "1 imported book at 12.49"
    product = Product(input)
    product.process()

    tax_applicator = TaxApplicator()
    tax_value = tax_applicator.apply_tax(product.name, product.price, product.imported)

    assert tax_applicator.round_up_price(tax_value) == 0.62

def test_apply_all_taxes():
    input = "1 imported perfume at 12.49"
    product = Product(input)
    product.process()

    tax_applicator = TaxApplicator()
    tax_value = tax_applicator.apply_tax(product.name, product.price, product.imported)

    assert tax_applicator.round_up_price(tax_value) == 1.94