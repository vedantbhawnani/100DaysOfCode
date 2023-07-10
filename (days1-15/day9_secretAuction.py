import os
import sys
import pyfiglet as pf
from termcolor import cprint
from colorama import init
init(strip=not sys.stdout.isatty())


def namee():
    cprint(pf.figlet_format("Secret Auction",
           font="starwars"), 'red', attrs=['bold'])


def cont():
    more = input("Are there any more bidders?\nType 'yes' or 'no': ")
    if more == "yes":
        os.system('cls')
        namee()
        return 1
    elif more == "no":
        return 0

    # else:
    #     print("Wrong input. Please input only 'yes' or 'no'. ")
    #     return cont()  # check this, doesnt work!!


# def get_key(bidders):
#     for key in bidders:
#         return key


def main():
    namee()
    bidders = {}
    moree = 1
    while moree == 1:
        name = input("What's your name? ")
        bidders[name] = input("Enter your bid. $ ")
        moree = cont()
    # first = get_key(bidders)
    # vale = bidders[first]
    # print(vale)
    sorted_bidders = sorted(
        bidders.items(), key=lambda kv: kv[1])
    bid = dict(sorted_bidders)
    # print(bid)
    first_pair = list(bid.items())[0]
    # print(first_pair)
    print(
        f"The auction is won by {first_pair[0]} with a bid of {first_pair[1]}.")


main()
