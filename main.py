"""Entry point: load data, run strategy, print performance."""
from src.backtester import Backtester
from src.data import DataLoader
from src.metrics import performance_summary
from src.strategy import MovingAverageStrategy


def main() -> None:
    prices = DataLoader(n_days=1000).load()
    backtester = Backtester(MovingAverageStrategy(fast=20, slow=50), cost=0.001)

    results = {
        "Strategy": backtester.run(prices),
        "Buy & Hold": prices.pct_change().fillna(0.0),
    }
    for name, returns in results.items():
        print(f"\n{name}")
        for metric, value in performance_summary(returns).items():
            print(f"  {metric:<18}{value:>9.3f}")


if __name__ == "__main__":
    main()
