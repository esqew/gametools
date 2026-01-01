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

### Bank
A currency store, especially useful for "scorekeeping" in gambling-style games
 
    from gametools.bank import PlayerBank

    player_bank = PlayerBank(starting_balance=200.00)
    player_bank.withdraw(125.00) # new balance: 75.00
    player_bank.deposit(100.00) # new balance: 175.00

