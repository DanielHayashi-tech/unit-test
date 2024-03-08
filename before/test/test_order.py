from pay.order import OrderStatus, LineItem, Order

def test_empty_order_total() -> None:
    '''
    if there is no line item given than order total == 0
    '''
    order = Order()
    assert order.total == 0

def test_order_total() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Ball", price=200))
    assert order.total == 200

def test_order_total() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Ball", price=200, quantity=2))
    assert order.total == 400

def test_order_status() -> None:
    order = Order()
    order.pay()
    assert order.status == OrderStatus.PAID

def test_order_status_not_paid() -> None:
    order = Order()
    assert order.status == OrderStatus.OPEN

