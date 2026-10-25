import json
from decimal import Decimal

from .types import Portfolio, ValuedPosition


def calculate_weights(positions: list[ValuedPosition]):
    portfolio_value = Decimal(0)
    for position in positions:
        portfolio_value += position["last_price"] * position["shares"]
    print("\nPortfolio value:", portfolio_value)

def read_portfolio():
    with open("./portfolio.json", "r") as file:
        portfolio: Portfolio = json.load(file, parse_float=Decimal)
        currency = portfolio["currency"]
        valued_positions = [
            ValuedPosition(**position, last_price=Decimal(0), ask_price=Decimal(0), current_weight=Decimal(0))
            for position in portfolio["positions"]
        ]
        for position in valued_positions:
            currency = position.get("currency", currency)
            position["last_price"], position["ask_price"] = map(Decimal,
                input(f'Enter the last price and ask price for {position['symbol']} ({currency}): ').split()
            )

        calculate_weights(valued_positions)

        # for position in valued_positions:
        #     print(f'Symbol {position["symbol"]} has weight {position["current_weight"]}')