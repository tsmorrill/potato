from random import randrange
import os


class Stat:
    def __init__(self, name):
        self.name = name
        self.value = 0

    def add(self, n):
        print(f"+{n}", self.name)
        self.value += n

    def remove(self, n):
        print(f"-{n}", self.name)
        self.value = max(0, self.value - n)


destiny = Stat("DESTINY")
potatoes = Stat("POTATO")
orcs = Stat("ORC")
ransom = Stat("RANSOM")
ransom.value = 1


def d6():
    return randrange(1, 7)


def main():
    while True:
        clear()
        event()
        if potatoes.value >= 10:
            print("You have enough potatoes that you can go underground and not return to the surface until the danger is past.")
            print("You nestle down into your burrow and enjoy your well earned rest.")
            break
        if orcs.value >= 10:
            print("Orcs finally find your potato farm.")
            print("Alas, orcs are not so interested in potatoes as they are in eating you, and you end up in a cookpot.")
            break
        if destiny.value >= 10:
            print("An interfering bard or wizard turns up at your doorstep with a quest, and you are whisked away against your will on an adventure")
            break
        next()
        if not bribable():
            print("")
            input("=>")
            print("")
        else:
            while bribable():
                r = ransom.value
                suffix = "ES"*int(potatoes.value >= 2)
                choice = input(f"Remove {r} POTATO{suffix} to remove 1 ORC? (y/n) ")
                if choice == "n":
                    break
                if choice == "y":
                    potatoes.remove(r)
                    orcs.remove(1)
    print("GAME OVER")


def bribable():
    return orcs.value > 0 and ransom.value <= potatoes.value


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def next():
    print("")
    print(f"{destiny.value} DESTINY")
    p = potatoes.value
    suffix = "ES"*int(p >= 2)
    print(f"{p} POTATO{suffix}")
    o = orcs.value
    suffix = "S"*int(o >= 2)
    print(f"{o} ORC{suffix}")


def event():
    roll = d6()
    if roll in {1, 2}:
        print("In the Garden...")
        print("")
        garden()
    elif roll in {3, 4}:
        print("A Knock at the Door...")
        print("")
        knock()
    elif roll in {5, 6}:
        print("The world becomes a darker, more dangerous place.")
        ransom.add(1)


def garden():
    roll = d6()
    if roll == 1:
        print("You happily root about all day in your garden.")
        print("")
        potatoes.add(1)
    elif roll == 2:
        print("You narrowly avoid a visitor by hiding in a potato sack.")
        print("")
        potatoes.add(1)
        destiny.add(1)
    elif roll == 3:
        print("A hooded stranger lingers outside your farm.")
        print("")
        destiny.add(1)
        orcs.add(1)
    elif roll == 4:
        print("Your field is ravaged in the night by unseen enemies.")
        print("")
        orcs.add(1)
        potatoes.remove(1)
    elif roll == 5:
        print("You trade potatoes for other delicious foodstuffs.")
        print("")
        potatoes.remove(1)
    elif roll == 6:
        print("You burrow into a bumper crop of potatoes. Do you cry with joy? Possibly.")
        print("")
        potatoes.add(2)


def knock():
    roll = d6()
    if roll == 1:
        print("A distant cousin. They are after your potatoes. They may snitch on you.")
        print("")
        orcs.add(1)
    elif roll == 2:
        print("A dwarven stranger. You refuse them entry. Ghastly creatures.")
        print("")
        destiny.add(1)
    elif roll == 3:
        print("A wizard strolls by. You pointedly draw the curtains.")
        print("")
        destiny.add(1)
        orcs.add(1)
    elif roll == 4:
        print("There are rumors of war in the reaches. You eat some potatoes.")
        print("")
        orcs.add(2)
        potatoes.remove(1)
    elif roll == 5:
        print("It's an elf. They are not serious people.")
        print("")
        destiny.add(1)
    elif roll == 6:
        print("It's a sack of potatoes from a generous neighbour.")
        print("You really must remember to pay them a visit one of these years.")
        print("")
        potatoes.add(2)


if __name__ == "__main__":
    main()
