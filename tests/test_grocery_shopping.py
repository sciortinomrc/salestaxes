from Pos import Pos

def test_scan_item_1():
    pos = Pos()
    input = "1 book at 12.49"
    pos.scan_item(input)
    product = pos.basket[0] 
    assert product.name == "1 book"
    assert product.price == 12.49
    assert product.taxed_price == 12.49

def test_scan_item_2():
    pos = Pos()
    input = "1 music CD at 14.99"
    pos.scan_item(input)
    product = pos.basket[0] 
    assert product.name == "1 music CD"
    assert product.price == 14.99
    assert product.taxed_price == 16.49

def test_scan_item_3():
    pos = Pos()
    input = "1 chocolate bar at 0.85"
    pos.scan_item(input)
    product = pos.basket[0] 
    assert product.name == "1 chocolate bar"
    assert product.price == 0.85
    assert product.taxed_price == 0.85

def test_scan_item_4():
    pos = Pos()
    input = "1 imported box of chocolates at 10.00"
    pos.scan_item(input)
    product = pos.basket[0] 
    assert product.name == "1 imported box of chocolates"
    assert product.price == 10.00
    assert product.taxed_price == 10.50

def test_scan_item_5():
    pos = Pos()
    input = "1 imported bottle of perfume at 47.50"
    pos.scan_item(input)
    product = pos.basket[0] 
    assert product.name == "1 imported bottle of perfume"
    assert product.price == 47.50
    assert product.taxed_price == 54.65


def test_produce_bill():
    pos = Pos()
    input1 = "1 book at 12.49"
    input2 = "1 music CD at 14.99"
    input3 = "1 chocolate bar at 0.85"
    pos.scan_item(input1)
    pos.scan_item(input2)
    pos.scan_item(input3)
    bill = pos.produce_bill()
    expected_bill = """1 book: 12.49
1 music CD: 16.49
1 chocolate bar: 0.85
Sales Taxes: 1.50
Total: 29.83"""

    assert bill == expected_bill
    

