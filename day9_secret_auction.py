def secret_auction():
    print("Gaval ascii art here...")
    auction_dict = {}

    #add name and bid into a dictionary as key and value
    while True:
        name_key =  str(input("enter your name: "))
        if name_key.lower() == 'done':
            break
        value_bid = int(input("enter your bid price: "))
        auction_dict[name_key] = value_bid

        highest_bid = max(auction_dict.values())
        highest_bidder = max(auction_dict, key=auction_dict.get)


        # continue and clear console else print higest bidder
        more_bids = str(input("are there any users left who want to bid? Type yes or no: ")).lower()
        if more_bids == 'yes':
            print('\n' * 100) 
            continue
        else:
            print(auction_dict)
            print(f"The highest bidder was {highest_bidder} with a whopping ${highest_bid}")
            break
              
secret_auction()
    