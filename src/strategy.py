"""Trading strategies."""
from abc import ABC, abstractmethod

import pandas as pd


class Strategy(ABC):
    """Base class: every strategy turns prices into a position series."""

    @abstractmethod
    def generate_signals(self, prices: pd.Series) -> pd.Series:
        """Return 1.0 (long) or 0.0 (flat) for each date."""


class MovingAverageStrategy(Strategy):
    """Long when the fast moving average is above the slow one."""

    def __init__(self, fast: int = 20, slow: int = 50) -> None:
        if fast >= slow:
            raise ValueError("fast window must be smaller than slow window")
        self.fast = fast
        self.slow = slow

    def generate_signals(self, prices: pd.Series) -> pd.Series:
        fast_ma = prices.rolling(self.fast).mean()
        slow_ma = prices.rolling(self.slow).mean()
        return (fast_ma > slow_ma).astype(float)
