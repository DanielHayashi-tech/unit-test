from pay.order import LineItem

def test_line_item_default() -> None:
    '''
    defualt quantity is 1

    price == total
    '''
    line_item = LineItem(name="test", price=100)
    assert line_item.total == 100

def test_line_item() -> None:
    line_item = LineItem(name="test", price=200, quantity=5)
    assert line_item.total == 1000