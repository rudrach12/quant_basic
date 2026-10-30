"""Performance metrics."""
import numpy as np
import pandas as pd

TRADING_DAYS = 252


def performance_summary(returns: pd.Series) -> dict:
    """Return key performance statistics for a daily return series."""
    equity = (1 + returns).cumprod()
    drawdown = equity / equity.cummax() - 1
    std = returns.std()
    return {
        "total_return": equity.iloc[-1] - 1,
        "annual_return": returns.mean() * TRADING_DAYS,
        "annual_volatility": std * np.sqrt(TRADING_DAYS),
        "sharpe": returns.mean() / std * np.sqrt(TRADING_DAYS) if std > 0 else 0.0,
        "max_drawdown": drawdown.min(),
    }
