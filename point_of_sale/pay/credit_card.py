from dataclasses import dataclass

@dataclass
class CreditCard:
    number: str
    expirey_month: int
    expirey_year: int