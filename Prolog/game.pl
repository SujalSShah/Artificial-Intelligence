% Facts
batsman(sachin).
bowler(bumrah).
bowler(shami).
captain(dhoni).
wicketkeeper(karthik).


% Rules
cricketer(X):-batsman(X).
cricketer(X):-bowler(X).
cricketer(X):-wicketkeeper(X).
cricketer(X):-captain(X).

player(X) :- cricketer(X).

