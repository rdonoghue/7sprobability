# 7sprobability
Generating some probability charts for the new 7th Sea die mechanic (which is giving me an excuse to dink around in python).

## Summary
7th Se die rolling works as follows:
1. Grab a pool of 10 sided dice. Size of the pool is usually stat plus skill plus other modifiers, but for the purposes of this roll it largely doesn't matter, except for the complications notede below.
2. Roll all the dice.
3. Try to build sets of 10 (so, a natural 10 would be one set, a 6 and a 4 could be a another set and so on)
4. You are allowed to build sets with a value higher than 10 (so 6,6 would be a valid set) and you can build sets out of however many dice you want (so 3,3,4 could be a set)
5. You always want to optimize for the most sets.  Thus, if you rolled "8,8,2,2" you would want to build two sets (8,2 and 8,2)
6. Leftover dice form an unused set. The values of the remaining dice are unimportant, but the number of unused dice matter for other game purposes.

### Complications
Skills are ranked from 1-5, and in addition to providing dice, they offer extra complications.
* If a character has 3 ranks, they may reroll one die
* if the character has 4 ranks, they may opt to build *2* raises by building sets on 15.
* if the character has 5 ranks, then 10's "explode", meaning that 10 is kept, and an additional die is rolled.

These effects stack, so at 5 ranks, a character may reroll, build on 15, and have their 10s explode.

## Goal
The goal of this project is twofold:
1. Create a die roller that takes the number of dice being rolled and the skill rank and returns the number of raises and remaining pool. It must do this intelligently enough to build the same number of sets that a human player would.

2. Once die rolling has been automated, use it to run Monte Carlo simulations of a wide array of pools and skill ranks, in order to see how the probabilities play out.  I lack the skill to graph this within python (at the moment) so the priority is to be able to export a .csv (or .csv friendly text) which I can then plug into a spreadsheet to do the graphing.
