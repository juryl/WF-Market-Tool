import pywmapi as wm
import numpy as np
import pandas as pd

def import_orders(sess):
    buy_orders, sell_orders = wm.orders.get_current_orders(sess)

    # Try import existing data to avoid overwriting active orders. If not there create entirely new DF.
    try: clean_buy_orders = pd.read_csv("buy_orders.csv")
    except: clean_buy_orders = pd.DataFrame(columns=("ID", "Price", "Order_Type", "Item_ID", "Item_Name", "Mod_Rank", "Active", "Min", "Max"))

    for x in range(len(buy_orders)):
        item = [0,0,0,0,0,0,0,0,0]
        item[0]=(buy_orders[x].id)
        item[1]=(buy_orders[x].platinum)
        item[2]=(buy_orders[x].order_type)
        item[3]=(buy_orders[x].item.id)
        item[4]=(buy_orders[x].item.url_name)
        item[5]=(buy_orders[x].item.mod_max_rank)
        item[6]=("False")

        # If conditional to check if order is already in dataframe
        duplicate = item[4] in clean_buy_orders["Item_Name"].values
        if(duplicate==False):
            clean_buy_orders.loc[len(clean_buy_orders)] = item
            print("Order Added")
        else:
            print("Duplicate Item")

        #print(clean_buy_orders[x], "\n")

    if len(clean_buy_orders)>len(buy_orders):
        #Loop to scan list of names in clean orders against ones in buy orders to find and delete outdated order. 
        count = 0
        for x in range(len(clean_buy_orders)):
            value_to_check = clean_buy_orders.at[x, "Item_Name"]
            exists = any(Orderitem.item.url_name == value_to_check for Orderitem in buy_orders)
            if exists == False: 
                print("False")
                try: clean_buy_orders.drop([x], inplace=True)
                except: print("Drop failed")
                count+=1

        print(count)
    
        
        


    clean_buy_orders.to_csv("buy_orders.csv", index=False)



    try: clean_sell_orders = pd.read_csv("sell_orders.csv")
    except: clean_sell_orders = pd.DataFrame(columns=("ID", "Price", "Order_Type", "Item_ID", "Item_Name", "Mod_Rank", "Active", "Min", "Max"))
#Extract Useful Information and construct list
    for x in range(len(sell_orders)):
        item = [0,0,0,0,0,0,0,0,0]
        item[0]=(sell_orders[x].id)
        item[1]=(sell_orders[x].platinum)
        item[2]=(sell_orders[x].order_type)
        item[3]=(sell_orders[x].item.id)
        item[4]=(sell_orders[x].item.url_name)
        item[5]=(sell_orders[x].item.mod_max_rank)
        item[6]=("False")

# If conditional to check if order is already in dataframe
        duplicate = item[4] in clean_sell_orders["Item_Name"].values
        if(duplicate==False):
            clean_sell_orders.loc[len(clean_sell_orders)] = item
            print("Order Added")
        else:
            print("Duplicate Item")

    if len(clean_sell_orders)>len(sell_orders):
            #Loop to scan list of names in clean orders against ones in buy orders to find and delete outdated order. 
            count = 0
            for x in range(len(clean_sell_orders)):
                value_to_check = clean_sell_orders.at[x, "Item_Name"]
                exists = any(Orderitem.item.url_name == value_to_check for Orderitem in sell_orders)
                if exists == False: 
                    print("False")
                    try: clean_sell_orders.drop([x], inplace=True)
                    except: print("Drop failed")
                    count+=1

            print(count)

            #print(clean_buy_orders[x], "\n")
    clean_sell_orders.to_csv("sell_orders.csv", index=False)
    return

