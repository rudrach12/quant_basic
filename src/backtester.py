"""Backtest engine."""
import pandas as pd

from src.strategy import Strategy


class Backtester:
    """Applies a strategy to prices and returns daily strategy returns."""

    def __init__(self, strategy: Strategy, cost: float = 0.001) -> None:
        self.strategy = strategy
        self.cost = cost  # fraction of traded value paid on each position change

    def run(self, prices: pd.Series) -> pd.Series:
        signals = self.strategy.generate_signals(prices)
        # Shift by one day: today's signal is traded tomorrow (no look-ahead bias).
        position = signals.shift(1).fillna(0.0)
        market_returns = prices.pct_change().fillna(0.0)
        turnover = position.diff().abs().fillna(0.0)
        return position * market_returns - turnover * self.cost
