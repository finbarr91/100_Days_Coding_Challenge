from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
bids = {}

finished_bidding = False


def find_highest_bidder(bidding_record):
    for bidder in bidding_record:

        #   key_list = list(bids.keys())
        #   value_list = list(bids.values())
        #   winner = max(value_list)
        #   position = value_list.index(winner)
        # print(f"{key_list[position]} is the winner of this auction with {winner} bid" )
        highest_bid = 0
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${bid_amount}")


while not finished_bidding:
    name = input("What is your name?\n")
    price = int(input("What is your bid Price?\n$"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Yes' or 'no' ")
    if should_continue == 'no'.lower():
        finished_bidding = True
        find_highest_bidder(bids)
    elif should_continue == 'yes'.lower():
        clear()


