import pandas as pd
import matplotlib.pyplot as plt
# back tests results on validation data
from matplotlib import rcParams

# Define font settings for Springer template
#rcParams['font.family'] = 'serif'
#rcParams['font.serif'] = ['Times New Roman']
rcParams['text.usetex'] = True
rcParams['font.size'] = 16
rcParams['mathtext.fontset'] = 'stix'
rcParams['font.family'] = 'STIXGeneral'

ep_30 = "models/PCN_sweep_sp_17_9s2d0yaa_9s2d0yaa/evaluation_metrics_front.csv"
ep_100 = "models/PCN_sweep_sp_17_y73vig0d_y73vig0d/evaluation_metrics_front.csv"
ep_252 = 'models/PCN_sweep_sp_17_vxj8pdbw_vxj8pdbw/evaluation_metrics_front.csv'
df = pd.read_csv(ep_30)
df2 = pd.read_csv(ep_100)
df3 = pd.read_csv(ep_252)


stocks = ['AAPL', 'MSFT', 'JNJ', 'PG', 'TSLA', 'NFLX', 'KO', 'V']
stocks = [x+" price" for x in stocks]
returns = []
for stock in stocks:
    returns = [f"{stock}_return"]
    df[f"{stock}_return"] = df[stock].pct_change().fillna(0)

df["market_return"] = df[returns].mean(axis=1)
initial_investment = df.loc[0, 'portfolio value']
df['cumulative portfolio return'] = (1 + df['market_return']).cumprod()
# Calculate the portfolio value over time
df['market value'] = initial_investment * df['cumulative portfolio return']
# df['portfolio volatility'] = abs(df['risk reward'])

date_range = pd.date_range(start='2020-08-24', periods=len(df), freq='B')
plt.figure(figsize=(14, 7))
plt.plot(date_range, df['portfolio value'], label='30-days episode based strategy')
plt.plot(date_range, df2['portfolio value'], label='100-days episode based strategy')
plt.plot(date_range, df3['portfolio value'], label='252-days episode based strategy')
plt.plot(date_range, df['market value'], label='Baseline', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Portfolio Value')
plt.title('Portfolio value for different episode length configurations in S\&P 500 base scenario')
plt.legend()
plt.grid(True)
plt.show()
print(df['transaction costs'].sum())
print(df2['transaction costs'].sum())
print(df3['transaction costs'].sum())
print(df2['actions'].value_counts())
print(df['AAPL price'].tail())




# plots for s&P extended
pcn = "models/PCN_sweep_sp_17_v0244b2c_v0244b2c/evaluation_metrics_backtest_validation.csv"
dqn = "models/DQN_sp_extended_17_06_15_24_d8hah8u1/evaluation_metrics_backtest_validation.csv"
ppo = "models/PPO_sp_extended_81_06_15_24_pcr0nder/evaluation_metrics_backtest_validation.csv"
df = pd.read_csv(dqn)
df2 = pd.read_csv(ppo)
df3 = pd.read_csv(pcn)


stocks = ['AAPL',
        'MSFT',
        'JNJ',
        'PG',
        'TSLA',
        'NFLX',
        'KO',
        'V',
        'GOOGL',
        'AMZN',
        'META',
        'JPM',
        'UNH',
        'HD',
        'VZ',
        'DIS',
        'NVDA',
        'MA',
        'ADBE',
        'IBM']
stocks = [x+" price" for x in stocks]
returns = []
for stock in stocks:
    returns = [f"{stock}_return"]
    df[f"{stock}_return"] = df[stock].pct_change().fillna(0)

df["market_return"] = df[returns].mean(axis=1)
initial_investment = df.loc[0, 'portfolio value']
df['cumulative portfolio return'] = (1 + df['market_return']).cumprod()
# Calculate the portfolio value over time
df['market value'] = initial_investment * df['cumulative portfolio return']
# df['portfolio volatility'] = abs(df['risk reward'])

date_range = pd.date_range(start='2020-08-24', periods=len(df), freq='B')
plt.figure(figsize=(14, 7))
plt.plot(date_range, df['portfolio value']/10, label='DQN')
plt.plot(date_range, df2['portfolio value']/10, label='PPO')
plt.plot(date_range, df3['portfolio value'], label='PCN')
plt.plot(date_range, df['market value']/10, label='Baseline', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Portfolio Value')
plt.title('Portfolio value for different models in S\&P 500 extended scenario')
plt.legend()
plt.grid(True)
plt.show()

# plots for crypto
# back tests results on validation data
dqn_c = "models/DQN_crypto_81_06_17_24_ca8svpca/evaluation_metrics_backtest_validation.csv"
ppo_c = "models/PPO_crypto_83_06_17_24_gzsbryxw/evaluation_metrics_backtest_validation.csv"
pcn_c = "models/PCN_sweep_sp_81_tlhm6t79_tlhm6t79/evaluation_metrics_backtest_validation.csv"
df = pd.read_csv(dqn_c)
df2 = pd.read_csv(ppo_c)
df3 = pd.read_csv(pcn_c)


stocks = ["BTC-USD", "ETH-USD", "LTC-USD", "XRP-USD", "XMR-USD", 
           "DASH-USD", "ETC-USD", "ZEC-USD", "DCR-USD", "WAVES-USD"]
stocks = [x+" price" for x in stocks]
returns = []
for stock in stocks:
    returns = [f"{stock}_return"]
    df[f"{stock}_return"] = df[stock].pct_change().fillna(0)

df["market_return"] = df["BTC-USD price_return"]
initial_investment = df.loc[0, 'portfolio value']
df['cumulative portfolio return'] = (1 + df['market_return']).cumprod()
# Calculate the portfolio value over time
df['market value'] = initial_investment * df['cumulative portfolio return']
# df['portfolio volatility'] = abs(df['risk reward'])

date_range = pd.date_range(start='2022-04-14', periods=len(df), freq='B')
plt.figure(figsize=(14, 7))
plt.plot(date_range, df['portfolio value']/10, label='DQN')
plt.plot(date_range, df2['portfolio value']/10, label='PPO')
plt.plot(date_range, df3['portfolio value']/10, label='PCN')
plt.plot(date_range, df['market value']/10, label='Baseline', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Portfolio Value')
plt.title('Portfolio value for different models in cryptocurrencies scenario')
plt.legend()
plt.grid(True)
plt.show()


