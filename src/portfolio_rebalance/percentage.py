import json
import requests
from decimal import Decimal

from .types import Portfolio, ValuedPosition, ExchangeRates

exchange_rates: ExchangeRates = {}

def fetch_exchange_rates(main_currency: str, other_currencies: list[str]):
    global exchange_rates
    if len(other_currencies) == 0:
        return
    response = requests.get("https://api.frankfurter.dev/v2/rates",params={
        "base": main_currency, "quotes": ",".join(other_currencies)
    }, timeout=10)
    response.raise_for_status()
    exchange_rates.update({
        item["quote"]: 1 / Decimal(str(item["rate"]))
        for item in response.json()
    })

    print("=== Fetched reference exchange rates ===")
    for currency, rate in exchange_rates.items():
        print(f"{currency}{main_currency} -> {rate:.6f}")
    print("")

def calculate_weights(positions: list[ValuedPosition]):
    portfolio_value = Decimal(0)
    for pos in positions:
        pos["current_value"] = pos["last_price"] * pos["shares"]
        if pos.get("currency"):
            pos["current_value"] *= exchange_rates[pos["currency"]]
        portfolio_value += pos["current_value"]

    for pos in positions:
        pos["current_weight"] = pos["current_value"] / portfolio_value

    print(f"\nPortfolio value: {portfolio_value:.2f}\n")

def read_portfolio():
    with open("./portfolio.json", "r") as file:
        portfolio: Portfolio = json.load(file, parse_float=Decimal)
        main_currency = portfolio["currency"]
        currencies = [pos["currency"] for pos in portfolio["positions"] if pos.get("currency")]
        fetch_exchange_rates(main_currency, currencies)
        valued_positions = [
            ValuedPosition(**position, last_price=Decimal(0), ask_price=Decimal(0), current_weight=Decimal(0))
            for position in portfolio["positions"]
        ]
        for position in valued_positions:
            currency = position.get("currency", main_currency)
            position["last_price"], position["ask_price"] = map(Decimal,
                input(f'Enter the last price and ask price for {position['symbol']} ({currency}): ').split()
            )

        calculate_weights(valued_positions)

        for position in valued_positions:
            print(f'Symbol {position["symbol"]} has weight {position["current_weight"]:.4f} with {position["shares"]} shares at {position["last_price"]:.2f}')