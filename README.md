# Portfolio Rebalance

A simple Python CLI tool that calculates how many shares to buy to rebalance a stock portfolio toward its target allocations.

The tool aims to invest as much available capital as possible while minimizing allocation deviations, without selling existing positions.

## Features

- Calculate current and projected portfolio allocations.
- Suggest share purchases based on available funds.
- Maximize invested capital while minimizing allocation deviations.
- Support multiple currencies and stock exchanges.
- Retrieve reference exchange rates from a public API.
- Account for actual currency conversion costs.
- Avoid selling existing positions.

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/csantv/portfolio-rebalance.git
cd portfolio-rebalance
uv sync
```

## Usage

Run the application with:

```bash
uv run portfolio-rebalance
```

## Configuration

Create a `portfolio.json` file from the provided example:

```bash
cp portfolio.example.json portfolio.json
```

Edit `portfolio.json` to define your positions, current share quantities, and target allocations.

```json
{
  "currency": "USD",
  "exchange": "NASDAQ",
  "positions": [
    {
      "symbol": "META",
      "shares": 20,
      "target": 0.40
    },
    {
      "symbol": "NVDA",
      "shares": 100,
      "target": 0.35
    },
    {
      "symbol": "SHEL",
      "shares": 40,
      "target": 0.25,
      "exchange": "LSE",
      "currency": "GBP"
    }
  ]
}
```

### Configuration fields

| Field | Description |
|---|---|
| `currency` | Default portfolio currency |
| `exchange` | Default stock exchange |
| `positions` | List of portfolio holdings |
| `symbol` | Stock or ETF ticker symbol |
| `shares` | Number of shares currently held |
| `target` | Desired portfolio allocation (0–1) |

Each position can optionally override the default `currency` and `exchange`.

Target allocations must sum to `1.0` (100%).

## License

See [LICENSE](LICENSE) for details.