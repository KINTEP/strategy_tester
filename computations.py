import numpy as np 
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import ADXIndicator

def sell_order(tp, sl, test_data):
    "We assume the entry price is first element in the data"
    profit = 0
    data = test_data[:]
    entry = test_data[0][-1]
    for i in range(1, len(data)):
        prev_px = data[i-1]
        next_px = data[i]
        diff = next_px[-1] - prev_px[-1]
        profit += diff
        if next_px[0] <= tp or next_px[1] <= tp  or next_px[2] <= tp:
            profit += tp - next_px[-1]
            break
        if next_px[0] >= sl or next_px[1] >= sl or next_px[2] >= sl:
            profit += sl - next_px[-1]
            break
    return -1*profit

def buy_order(tp, sl, test_data):
    "We assume the entry price is first element in the data"
    profit = 0
    data = test_data[:]
    entry = test_data[0][-1]
    for i in range(1, len(data)):
        prev_px = data[i-1]
        next_px = data[i]
        diff = next_px[-1] - prev_px[-1]
        profit += diff
        if next_px[0] >= tp or next_px[1] >= tp  or next_px[2] >= tp:
            profit += tp - next_px[-1]
            break
        if next_px[0] <= sl or next_px[1] <= sl or next_px[2] <= sl:
            profit += sl - next_px[-1]
            break
            
    return profit

def buy_without_sl(data, start):
    px = data[0]
    balances = []
    balance = start
    for i in range(len(data)-1):
        curr_px = data[i+1]
        prev_px = data[i]
        profit = 0.1*(curr_px - prev_px)
        if balance <= 0:
            break
        balance += profit
        balances.append(balance)
    return balance, i, balances

def buy_rules(rs, ad, pv, smh, px):
    dict1 = {}
    N = len(px)
    for i in range(N):
        if smh[i] > px[i] and px[i] > pv[i] and rs[i] > 55 and ad[i] > 25:
            dict1[i] = px[i]
    return dict1


def buy_rule(rs, ad, pv, smh, px):
    if smh > px and px > pv and rs > 55 and ad > 25:
        return True
    else:
        return False


def sell_rules(rs, ad, pv, sml, px):
    dict1 = {}
    N = len(px)
    for i in range(N):
        if sml[i] < px[i] and px[i] < pv[i] and rs[i] < 45 and ad[i] > 25:
            dict1[i] = px[i]
    return dict1

def sell_rule(rs, ad, pv, sml, px):
    if sml < px and px < pv and rs < 45 and ad > 25:
        return True
    else:
        return False