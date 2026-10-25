from decimal import Decimal
from typing import NotRequired, TypedDict


class Portfolio(TypedDict):
    currency: str
    exchange: str
    positions: list[Position]

class Position(TypedDict):
    symbol: str
    shares: int
    target: Decimal
    currency: NotRequired[str]
    exchange: NotRequired[str]

class ValuedPosition(Position):
    last_price: Decimal
    ask_price: Decimal
    current_value: Decimal
    current_weight: Decimal

type ExchangeRates = dict[str, Decimal]