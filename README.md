
# PhantomisForced with maths

This is a Python script that includes several functions to help with calculations related to the [Phantom Forces](https://www.roblox.com/games/292439477) game. The functions available are:

### `roundNum(number, place)`

Returns the input `number` rounded up to the nearest multiple of `place`.

### `nextReward(rank)`

Returns the amount of credits the player will receive with the next rank, given the current `rank`.

### `rankCredit(rank)`

Returns the total amount of credits the player will have earned by the given `rank`.

### `reducedPrice(gunRank, currentRank)`

Returns the reduced price for a `gunRank` weapon, given the player's current `currentRank`.

### `rankForgun(gunRank)`

Returns the rank the player needs to have to be able to purchase a `gunRank` weapon without using any credits. Note that MVPs and skins are not included.

### `rankForXP(currentRank=0, rank=1)`

Returns the amount of XP needed to rank up from `currentRank` to `rank`. If `currentRank` is not specified, it defaults to 0.

## Usage

The script includes an argparse module for command line usage. The available options are:

### `-rC/--rankCredit`

Gives the amount of credits the player should have by the given rank. Example usage: `python script.py -rC 50`

### `-rP/--reducedPrice`

Gives the reduced price for a `gunRank` weapon at the player's current rank. Example usage: `python script.py -rP 10,40`

### `-nR/--nextReward`

Gives the amount of credits the player will receive with the next rank. Example usage: `python script.py -nR 10`

### `-rFg/--rankForgun`

Gives the rank the player needs to be to purchase a `gunRank` weapon without using any credits. Example usage: `python script.py -rFg 20`

### `-rXP/--rankForXP`

Gives the amount of XP needed to rank up to the given rank from the player's current rank. If the current rank is not specified, it defaults to 0. Example usage: `python script.py -rXP 10,5`

The output of the selected function will be printed to the console.