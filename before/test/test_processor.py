from pay.processor import PaymentProcessor
import pytest

API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"

def test_invalid_api_key() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge(card="1249190007575069", month=12, year=2026, amount=600)

def test_valid_card_date() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge(card="1249190007575069", month=12, year=2026, amount=600)


def test_invalid_card_date() -> None:
    '''
    set an inproper year that provides a ValueError to:
     
    datetime(year, month, 1) > datetime.now()
    '''
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge(card="1249190007575069", month=12, year=2022, amount=600)

def test_invalid_card_number_luhn() -> None:
    ''''
    give an incorrect card number accroding to luhn's algorithm
    '''
    processor = PaymentProcessor(API_KEY)
    assert not processor.luhn_checksum(card_number="1249190007575068")

def test_valid_card_number_luhn() -> None:
    ''''
    give an incorrect card number accroding to luhn's algorithm
    '''
    processor = PaymentProcessor(API_KEY)
    assert processor.luhn_checksum(card_number="1249190007575069")
    