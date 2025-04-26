The purpose of this tool is to read the users Warframe Market orders via the website API, save them locally for editing, then to micromanage those orders to be at the top of the Warframe Market listings by adjusting the price to always be the same as the best offer. 

To use this tool, edit main.py and input your email address and password. Then run the program once to generate .csv files containing your orders. From here you determine which orders the program should manage by changing the active column to True and setting the minimum and maximum thresholds for that order. 

Haven't tested how the tool handles arcanes and mods yet since I'm only using it for rime parts atm. 

Not really interested in contributions or help, since this is a personal project I'm doing to learn python, but I'm happy for anyone to fork it and do their own thing with it.
