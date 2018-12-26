`game played in python shell`
1. There are two teams, A and T. Pick how many players you want on EACH team.
2. Then, you will be presented with a string of 2 times that number plus two empty positions('seats'). On top are their position numbers.
   Position numbers after 9 are printed as single digits above the players but should be typed as 10,11,12,...
3. The aim of the game is to get all players from team T sitting together and all team A players sitting together.

`When prompted for a command, you can enter:`
An integer: must be a players position number. This will replace the 2  empty seats with the player at the position you typed
            as well as the player to the right of this player. These 2 players' positions will be replaced by the empty underscores. Keep 
            entering position numbers and try to get the players sitting with there team. The final seating should be as follows:
            TTTTTAAAAA__    (5 players on each team)
            or
            AAAAATTTTT__

'b': undo move.

'q': quit game.
