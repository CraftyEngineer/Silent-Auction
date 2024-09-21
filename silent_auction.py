condition=True
bid_data={}

def function(bid_data):
  greatest_bid=0
  greatest_bidder=""
  for key in bid_data:
    if bid_data[key]>greatest_bid:
      greatest_bid=bid_data[key]
      greatest_bidder=key
  print(f"The greatest bid is ${greatest_bid}and is made by {greatest_bidder}")

while condition:
  name=input("Enter your name: ")
  bid=int(input("Enter your bid: $"))
  bid_data[name]=bid
  choice=input("Do you want to continue?: ").lower()
  if choice=="yes":
    condition=True
    # print("\n"*200)
  else:
    condition=False
    function(bid_data)