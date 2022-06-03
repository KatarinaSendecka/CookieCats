# CookieCats

Example of mobile game A/B test analysis. AD postponed from level 30 (A variant) to level 40 (B variant).

## Dataset:
- userid - A unique number that identifies each player.
- version - Whether the player was put in the control group (gate_30 - a gate at level 30) or the
- group with the moved gate (gate_40 - a gate at level 40).
- sum_gamerounds - The number of game rounds played by the player during the first 14 days
- after install.
- retention_1 - Did the player come back and play 1 day after installing?
- retention_7 - Did the player come back and play 7 days after installing?
