from random import randrange
import os


class Stat:
    def __init__(self, singular, plural):
        self.singular = singular
        self.plural = plural
        self.value = 0

    def name(self, n):
        if n == 1:
            return self.singular
        else:
            return self.plural

    def print(self):
        n = self.value
        print(f"{n} {self.name(n)}")

    def add(self, n):
        print(f"+{n} {self.name(n)}")
        self.value += n

    def remove(self, n):
        print(f"-{n} {self.name(n)}")
        self.value = max(0, self.value - n)


version = "1 tate 0"

destiny = Stat("DESTINY", "DESTINY")
potatoes = Stat("POTATO", "POTATOES")
orcs = Stat("ORC", "ORCS")
darkness = Stat("DARKNESS", "DARKNESS")
darkness.value = 1
secret = False


if os.name == 'nt':
    clear_string = 'cls'
else:
    clear_string = 'clear'


def clear():
    os.system(clear_string)


def d6():
    return randrange(1, 7)


def pause():
    print("")
    input("Press Enter to Continue.")


def main():
    title()
    while True:
        clear()
        event()
        print_stats()
        if max(potatoes.value, orcs.value, destiny.value) >= 10:
            break
        bribe()
    pause()
    end()


def title():
    length = 67 - len(version)
    clear()
    print("   ▄███████▄  ▄██████▄      ███        ▄████████     ███      ▄██████▄ ")
    print("  ███    ███ ███    ███ ▀█████████▄   ███    ███ ▀█████████▄ ███    ███")
    print("  ███    ███ ███    ███    ▀███▀▀██   ███    ███    ▀███▀▀██ ███    ███")
    print("  ███    ███ ███    ███     ███   ▀   ███    ███     ███   ▀ ███    ███")
    print("▀█████████▀  ███    ███     ███     ▀███████████     ███     ███    ███")
    print("  ███        ███    ███     ███       ███    ███     ███     ███    ███")
    print("  ███        ███    ███     ███       ███    ███     ███     ███    ███")
    print(" ▄████▀       ▀██████▀     ▄████▀     ███    █▀     ▄████▀    ▀██████▀ ")
    print(" "*length, "v.", version)
    print("")
    print("You are a halfling, just trying to exist.")
    print("Meanwhile, the Dark Lord rampages across the world.")
    print("You do not care about this. You are trying to farm potatoes.")
    print("Because what could a halfling possibly do about it anyway?")
    print("")
    print("Design by Oliver Darkshire -- https://twitter.com/deathbybadger")
    print("Code by Tammy Morrill -- https://github.com/tsmorrill")
    pause()


def event():
    roll = d6()
    if roll in {1, 2}:
        print("In the Garden...")
        print("")
        garden()
        print("")
    elif roll in {3, 4}:
        print("A Knock at the Door...")
        print("")
        knock()
        print("")
    elif roll in {5, 6}:
        print("The World becomes a Darker, more Dangerous Place.")
        print("")
        darkness.add(1)
        print("")
        darkness.print()


def garden():
    roll = d6()
    if roll == 1:
        print("You happily root about all day in your garden.")
        print("")
        potatoes.add(1)
    elif roll == 2:
        print("You narrowly avoid a visitor by hiding in a potato sack.")
        print("")
        destiny.add(1)
        potatoes.add(1)
    elif roll == 3:
        print("A hooded stranger lingers outside your farm.")
        print("")
        destiny.add(1)
        orcs.add(1)
    elif roll == 4:
        print("Your field is ravaged in the night by unseen enemies.")
        print("")
        potatoes.remove(1)
        orcs.add(1)
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
        potatoes.remove(1)
        orcs.add(2)
    elif roll == 5:
        print("It's an elf. They are not serious people.")
        print("")
        destiny.add(1)
    elif roll == 6:
        print("It's a sack of potatoes from a generous neighbour.")
        print("")
        print("You really must remember to pay them a visit one of these years.")
        print("")
        potatoes.add(2)


def print_stats(show_darkness=False):
    destiny.print()
    potatoes.print()
    orcs.print()


def bribe():
    def possible():
        return orcs.value > 0 and darkness.value <= potatoes.value
    print("")
    if not possible():
        input("Press Enter to Continue.")
    else:
        r = darkness.value
        while possible():
            choice = input(
                f"Give up {r} {potatoes.name(r)} to remove 1 ORC? (Press Enter to Skip.) ")
            if choice.lower() in {"y", "yes", "yes.", "give up"}:
                print("")
                potatoes.remove(r)
                orcs.remove(1)
                print("")
                print_stats()
                if not possible():
                    pause()
            else:
                if choice == "Bombadil":
                    global secret
                    secret = True
                break


def end():
    clear()
    if secret:
        print("An interruption. Your cousin begs you let him be the Dark Lord again.")
        print("")
        print("Yes, he makes a decent bad guy, but he doesn't have to be so MEAN about it.")
        print("")
        print("You return to playing with your toy farm on the bard's kitchen floor.")
    elif potatoes.value >= 10:
        print("There are enough potatoes that you can go underground 'til danger is past.")
        print("")
        print("You nestle down into your burrow and enjoy your well earned rest.")
    elif orcs.value >= 10:
        print("Orcs finally find your potato farm.")
        print("")
        print("Alas, orcs are not so interested in potatoes as they are in eating you.")
    elif destiny.value >= 10:
        print("An interfering bard or wizard turns up at your doorstep with a quest.")
        print("")
        print("You are whisked away against your will on an adventure.")
    print("")
    print("GAME OVER")
    print("")


if __name__ == "__main__":
    main()
