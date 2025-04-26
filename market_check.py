import pywmapi as wm
import numpy as np
import pandas as pd

def check_buy(name, min, max):

    orders = wm.items.get_orders(name)
    list = []
    #print(orders[0].user.status.value)
    #print(orders[0].order_type.value)
    for x in range(len(orders)):
        a = (orders[x].user.status.value)
        b = (orders[x].order_type.value)
        #print(a, ", ", b, "\n")
        #print("\n")
        if b == 'buy' and a == 'ingame':
            list.append(orders[x].platinum)
            #print("appending", "\n")

    list.sort(reverse=True)
    #print(len(list))
    #print(list[0:20])

    price = 0
    for x in range(len(list)):
        if list[x] > max: continue
        elif list[x]>price: price = list[x]
        
        #For efficiency end early one first price in valid range is found 
        if price > min: break
    
    #Set price to min if below min threshold
    if price<min: price = min
    

    return(price)

def check_sell(name, min, max):

    orders = wm.items.get_orders(name)
    list = []
    #print(orders[0].user.status.value)
    #print(orders[0].order_type.value)
    for x in range(len(orders)):
        a = (orders[x].user.status.value)
        b = (orders[x].order_type.value)
        #print(a, ", ", b, "\n")
        #print("\n")
        if b == 'sell' and a == 'ingame':
            list.append(orders[x].platinum)
            #print("appending", "\n")

    list.sort(reverse=False)
    #print(len(list))
    #print(list[0:20])

    price = max
    for x in range(len(list)):
        if list[x] < min: continue
        elif list[x]<price: price = list[x]
        
        #For efficiency end early one first price in valid range is found 
        if price < max: break
    
    #Set price to min if below min threshold
    if price>max: price = max
    

    return(price)
