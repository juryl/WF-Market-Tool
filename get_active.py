import pywmapi as wm
import numpy as np
import pandas as pd



def get_active():
    buy_orders = pd.read_csv("buy_orders.csv")

    #active_count = 0
    active_list = []
    for i in range(len(buy_orders)):
        active = buy_orders.loc[[i],["Active"]].bool()
        #print(active)
        if active is True:
            #print("test_cond")
            active_list.append(buy_orders.loc[i])
    

    active_buy_orders = pd.DataFrame(active_list, columns=buy_orders.columns)
    
    sell_orders = pd.read_csv("sell_orders.csv")
    

    #active_count = 0
    active_slist = []
    for i in range(len(sell_orders)):
        active = sell_orders.loc[[i],["Active"]].bool()
        #print(active)
        if active is True:
            #print("test_cond")
            active_list.append(sell_orders.loc[i])
    

    active_sell_orders = pd.DataFrame(active_slist, columns=buy_orders.columns)

    #print(active_buy_orders.head())
    return [active_buy_orders, active_sell_orders]
        

