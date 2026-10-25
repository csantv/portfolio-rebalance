import json
from .types import Portfolio, ValuedPosition


def calculate_weights(positions: list[ValuedPosition]):
    portfolio_value = 0
    for position in positions:
        portfolio_value += position["price"] * position["shares"]
    print("\nPortfolio value:", portfolio_value)

def read_portfolio():
    with open("./portfolio.json", "r") as file:
        portfolio: Portfolio = json.load(file)
        currency = portfolio["currency"]
        valued_positions = [
            ValuedPosition(**position, price=0, current_weight=0)
            for position in portfolio["positions"]
        ]
        for position in valued_positions:
            currency = position.get("currency", currency)
            position["price"] = float(input(f"Enter the price for {position['symbol']} ({currency}): "))

        calculate_weights(valued_positions)

        # for position in valued_positions:
        #     print(f'Symbol {position["symbol"]} has weight {position["current_weight"]}')