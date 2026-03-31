from random import choice

def flip_coin():
    coin_flip = choice(["Heads", "Tails"])
    print(f"You flipped {coin_flip}. ")
    if coin_flip == "Heads":
        print("You won!")
    else:
        print("You lost :(")
        