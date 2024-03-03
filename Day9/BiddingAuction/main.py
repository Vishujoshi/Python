import os
cls = lambda: os.system('cls')
import art

bid_dict={}
max=0
maxBidder=""
print(art.logo)
print("Wlecome to the Screen auction Program ")


keep_going=True
while keep_going:
    name=input("What is your name? ")
    bid=int(input("Enter your Bid : "))
    bid_dict[name]=bid
    more_users=input("Are There any bidders ? Type yes or no ")
    cls()
    if more_users=="no":
        keep_going=False
        for key in bid_dict:
            if bid_dict[key]>max:
                max=bid_dict[key]
                maxBidder=key
# print(bid_dict)

print(f"The winner is {maxBidder} with bid {max}")

