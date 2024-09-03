import pandas as pd
import glob
import os
import matplotlib.pyplot as plt

etf_code = '588000'
interval = 600
profit = 0.0
dir = f'/home/hejiayan/shannon_py_public/{etf_code}ETF finish/iopv&p/'
# 使用 glob 获取所有 CSV 文件的路径
csv_files = glob.glob(dir + '*.csv')  
profits = []    
csv_files.sort()
profit = 0.0  # Reset profit for each interval
for file in csv_files:
    df = pd.read_csv(file)
    line_index = 20
    i = 20
    times = 1
    date = os.path.basename(file)[:8]
    while line_index <= 14219 and times <= 1:
        if df['ask_iopvs'].iloc[line_index] < df['BidPrice'].iloc[line_index]:
            profit += ((df['BidPrice'].iloc[line_index] - df['ask_iopvs'].iloc[line_index]) / df['ask_iopvs'].iloc[line_index])
            print(date, 1, line_index, df['BidPrice'].iloc[line_index], df['ask_iopvs'].iloc[line_index],(df['BidPrice'].iloc[line_index] - df['ask_iopvs'].iloc[line_index]) / df['ask_iopvs'].iloc[line_index])
            line_index += 600
            times += 1
        elif df['bid_iopvs'].iloc[line_index] > df['AskPrice'].iloc[line_index] and df['AskPrice'].iloc[line_index] != 0:
            profit += ((df['bid_iopvs'].iloc[line_index] - df['AskPrice'].iloc[line_index]) / df['AskPrice'].iloc[line_index])
            print(date, 2, line_index, df['bid_iopvs'].iloc[line_index], df['AskPrice'].iloc[line_index], (df['bid_iopvs'].iloc[line_index] - df['AskPrice'].iloc[line_index]) / df['AskPrice'].iloc[line_index])
            line_index += 600
            times += 1
        else:
            line_index += 1

annualized_profit = profit / 117 / 3 * 250
print(annualized_profit)

