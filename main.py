import pywmapi as wm
import numpy as np
import pandas as pd
import import_orders
import get_active
import market_check
import warnings
import time
# Suppress FutureWarning messages
warnings.simplefilter(action='ignore', category=FutureWarning)

#Login with WFMarket ID
sess = wm.auth.signin("Email", "Password")

import_orders.import_orders(sess)
active_buy_orders, active_sell_orders = get_active.get_active()
count = 0
while(True): #Use Keyboard Interrupt || Make better interrupt in future 

    #Loop to run through active orders and update them according to market price
    for x in range(len(active_buy_orders)):
        name = active_buy_orders.at[x,"Item_Name"] #take from active orders df
        min = active_buy_orders.at[x,"Min"]
        max = active_buy_orders.at[x,"Max"]
        price = int(market_check.check_buy(name, min, max))


        new_item = wm.orders.OrderUpdateItem(
            platinum=price, 
            quantity=1 , 
            visible=True, 
            rank=None,       #active_buy_orders.at[x, "Mod_Rank"], 
            subtype=None)
        updated_order = wm.orders.update_order(
            sess=sess, 
            order_id=active_buy_orders.at[x,"ID"],
            updated_item=new_item)

        active_buy_orders.at[x, "Price"] = price
        time.sleep(1)
        #print("Order Updated","\n",updated_order, "\n\n")
    
    for x in range(len(active_sell_orders)):
        name = active_sell_orders.at[x,"Item_Name"] #take from active orders df
        min = active_sell_orders.at[x,"Min"]
        max = active_sell_orders.at[x,"Max"]
        price = int(market_check.check_sell(name, min, max))


        new_item = wm.orders.OrderUpdateItem(
            platinum=price, 
            quantity=1 , 
            visible=True, 
            rank=None,       #active_sell_orders.at[x, "Mod_Rank"], 
            subtype=None)
        updated_order = wm.orders.update_order(
            sess=sess, 
            order_id=active_sell_orders.at[x,"ID"],
            updated_item=new_item)

        active_sell_orders.at[x, "Price"] = price
        time.sleep(1)
        #print("Order Updated","\n",updated_order, "\n\n")

    print("\n","Cycle:", count)
    count += 1
    time.sleep(30)
print("\n","end")



