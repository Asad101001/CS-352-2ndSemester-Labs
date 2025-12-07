from Teddy import EngineDriver,Gardner

from Bunny import Clown,BankManager

def main():
    toys = [
        EngineDriver("Small"),
        Gardner("Large"),
        Clown("Medium"),
        BankManager("Tiny")
        ]

    for toy in toys:
        toy.make_noise()
        toy.get_bio()

if __name__ == "__main__":
    main()
