import yfinance as y
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


microsoft = y.Ticker("MSFT")

hist = microsoft.history("1mo")

msft_close = hist['Close']
msft = np.array(msft_close)

plt.plot(np.arange(1,22),msft)

plt.show()
