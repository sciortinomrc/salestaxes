import logging
from Product import Product
from ExemptionChecker import ExemptionChecker
from TaxApplicator import TaxApplicator
log = logging.getLogger("test.tax_exemption")

def test_book_tax_exempt():
  log.info("Verify that book is tax exempt, and it is")

  input = "1 book at 12.49"
  product = Product(input)
  product.process()
  exemption_checker = ExemptionChecker()
  result = exemption_checker.is_product_tax_exempt(product.name)
  assert result == True

def test_food_tax_exempt():
  log.info("Verify that chocolate is tax exempt, and it is")

  input = "1 chocolate bar at 0.85"
  product = Product(input)
  product.process()
  exemption_checker = ExemptionChecker()
  result = exemption_checker.is_product_tax_exempt(product.name)
  assert result == True

def test_medicine_tax_exempt():
  log.info("Verify that pills are tax exempt, and it is")

  input = "1 packet of headache pills at 9.75"
  product = Product(input)
  product.process()
  exemption_checker = ExemptionChecker()
  result = exemption_checker.is_product_tax_exempt(product.name)
  assert result == True

def test_perfume_not_tax_exempt():
  log.info("Verify that perfume is tax exempt, and it is not")

  input = "1 imported bottle of perfume at 27.99"
  product = Product(input)
  product.process()
  exemption_checker = ExemptionChecker()
  result = exemption_checker.is_product_tax_exempt(product.name)
  assert result == False

def test_apply_import_tax_to_exempt_product():
  input = "1 box of imported chocolates at 11.25"
  product = Product(input)
  product.process()

  tax_applicator = TaxApplicator()
  tax_value = tax_applicator.apply_import_tax(product.price, product.imported)
  tax_value = tax_applicator.round_up_price(tax_value)
  assert round(tax_value, 2) == 0.55