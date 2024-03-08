import os
import pytest
from datetime import date
from dotenv import load_dotenv

from pay.credit_card import CreditCard
from pay.processor import PaymentProcessor, luhn_checksum

load_dotenv()

API_KEY = os.getenv("API_KEY") or ""

CC_YEAR = date.today().year + 2

@pytest.fixture
def processor() -> PaymentProcessor:
    return PaymentProcessor(API_KEY)

def test_invalid_api_key() -> None:
    with pytest.raises(ValueError):
        card = CreditCard("1249190007575069", 12, CC_YEAR)
        PaymentProcessor("").charge(card, 100)

def test_valid_api_key() -> None:
    card = CreditCard("1249190007575069", 12, CC_YEAR)
    PaymentProcessor(API_KEY).charge(card, 100)


def test_valid_card_date(processor: PaymentProcessor) -> None:
    card = CreditCard("1249190007575069", 12, CC_YEAR)
    processor.charge(card, amount=100)


def test_invalid_card_date(processor: PaymentProcessor) -> None:
    with pytest.raises(ValueError):
        card = CreditCard("1249190007575069", 12, 2022)
        processor.charge(card, amount=100)

def test_valid_card_number_luhn():
    assert luhn_checksum("1249190007575069")

def test_invalid_card_number_luhn():
    assert not luhn_checksum("1249190007575068")

    