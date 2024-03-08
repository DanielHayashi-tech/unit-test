from datetime import datetime


class PaymentProcessor:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def _check_api_key(self) -> bool:
        return self.api_key == "6cfb67f3-6281-4031-b893-ea85db0dce20"

    def charge(self, card: str, month: int, year: int, amount: int) -> None:
        if not self.validate_card(card, month, year):
            raise ValueError("Invalid card")
        if not self._check_api_key():
            raise ValueError("Invalid API key")
        print(f"Charging card number {card} for ${amount/100:.2f}")

    def validate_card(self, card: str, month: int, year: int) -> bool:
        '''
        verifies that the card is legit (luhn_checksum) then verifies that the card is not expired.
        '''
        return self.luhn_checksum(card) and datetime(year, month, 1) > datetime.now()

    def luhn_checksum(self, card_number: str) -> bool:
        '''
        Luhn's algorithm (or Luhn's formula or Luhn's key) is a verification algorithm used to validate various numbers (such as credit cards).

        What is the Luhn Algorithm for?
        Luhn makes it possible to check numbers (credit card, gift card, IMEI, etc.) thanks to its control key (a digit which makes it possible to check the others digits).
        Example: 12345674 is a valid card number, 1234567 is the initial number and 4 is the checksum.
        '''
        def digits_of(card_nr: str):
            return [int(d) for d in card_nr]

        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for digit in even_digits:
            checksum += sum(digits_of(str(digit * 2)))
        return checksum % 10 == 0