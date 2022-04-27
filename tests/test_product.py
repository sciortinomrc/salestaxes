import logging
from Product import Product
log = logging.getLogger("test.product")
def test_new_product():
  log.info("Create a new product, it is generated correctly")

  input = "1 book at 12.49"
  product = Product(input)
  product.process()

  assert product.name == "book"
  assert product.price == 12.49
  assert product.type == "entertainment"
  assert product.category == "books"

def test_product_not_imported():
  log.info("Create a new product not imported, it is generated correctly")

  input = "1 book at 12.49"
  product = Product(input)
  product.process()

  assert product.name == "book"
  assert product.price == 12.49
  assert product.imported == False
  assert product.type == "entertainment"
  assert product.category == "books"

def test_product_imported():
  log.info("Create a new product imported, it is generated correctly")

  input = "1 imported bottle of perfume at 27.99"
  product = Product(input)
  product.process()

  assert product.name == "imported bottle of perfume"
  assert product.price == 27.99
  assert product.imported == True
  assert product.type == "chemicals"
  assert product.category == "personal_care"


    
