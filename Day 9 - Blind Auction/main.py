import art
print(art.logo)
bidding = True
highest_bid = 0
bids = {}
while bidding:
  name = input("What is your name?\n")
  bid = int(input("What is your bid?\n$"))
  bids[name] = bid
  if highest_bid < bid:
    highest_bid = bid
    winner = name
  other_bidders = input("Are there other bidders? Type 'Yes' or 'No'\n").lower()
  if other_bidders == "no":
    bidding = False
print(f"The winner is {winner} with a bid of ${highest_bid}")