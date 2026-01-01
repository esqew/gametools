# gametools.py
A collection of Python data structures and algorithms useful in game-type applications.

## Concepts & examples
### Dice
The classic throwable RNG from all your favorite board games.

    from gametools.dice import StandardDie

    die = StandardDie(sides=6)
    die.roll() # a random integer between 1-6
    print(die) # unicode representation of rolled value, i.e. ⚀

### Cards
    from gametools.cards import StandardDeck

    deck = StandardDeck().shuffle()
    print(deck) # 