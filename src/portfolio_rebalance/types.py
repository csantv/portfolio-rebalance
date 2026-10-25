from typing import NotRequired, TypedDict


class Portfolio(TypedDict):
    currency: str
    exchange: str
    positions: list[Position]

class Position(TypedDict):
    symbol: str
    shares: int
    target: float
    currency: NotRequired[str]
    exchange: NotRequired[str]

class ValuedPosition(Position):
    price: float
    current_weight: float