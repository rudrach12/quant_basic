"""Price data generation."""
import numpy as np
import pandas as pd


class DataLoader:
    """Produces a clean price series. Synthetic here; swap for real data later."""

    def __init__(self, n_days: int = 1000, seed: int = 42) -> None:
        self.n_days = n_days
        self.seed = seed

    def load(self) -> pd.Series:
        rng = np.random.default_rng(self.seed)
        daily_returns = rng.normal(0.0003, 0.01, self.n_days)
        dates = pd.bdate_range("2020-01-01", periods=self.n_days)
        prices = 100 * np.exp(np.cumsum(daily_returns))
        return pd.Series(prices, index=dates, name="price")
