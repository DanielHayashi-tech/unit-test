from pay.order import LineItem, Order
from pay.payment import pay_order
from pay.processor import PaymentProcessor
from pytest import MonkeyPatch
import pytest

def test_pay_order(monkeypatch: MonkeyPatch) -> None:
    def mock_charge(self: PaymentProcessor, card: str, month: int, year: int, amount: int) -> None:
        pass
    inputs = ["1249190007575069", 10, 2028]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0)) # this is not ideal
    monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True) # this is not ideal
    monkeypatch.setattr(PaymentProcessor, "charge", mock_charge) # this is not ideal
    order = Order()
    order.line_items.append(LineItem(name="test", price=10))
    pay_order(order)


def test_pay_order_invalid(monkeypatch: MonkeyPatch) -> None:
    '''
    ValueError: Can't pay an order with total 0 - there are no line items
    '''
    with pytest.raises(ValueError):
        inputs = ["1249190007575069", 10, 2028]
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0)) # this is not ideal
        monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True) # this is not ideal
        order = Order()
        pay_order(order)