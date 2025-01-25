from art import logo
print(logo)

#Dictionary to store the names and their respective bids
bid_dict = {
    "" : 0
}

rerun = 1

while rerun == 1:
    name = input("What's Your name:\n")
    bid_dict[name] = int(input("How much do you want to bid:\n$"))
    rerun = int(input("Are there anymore bidders?(Type '1' for yes and '2' for no):\n"))
    if rerun == 1:
        print("\n" * 100)
    elif rerun == 2:
        highest_bidder = ""
        bid_1 = ""
        bid_2 = ""
        for key in bid_dict:
            bid_1 = bid_2
            bid_2 = key
            if bid_dict[bid_1] << bid_dict[bid_2]:
                highest_bidder = key
            else:
                highest_bidder = bid_1

print(f"************************************THE WINNER IS {highest_bidder}!!************************************")