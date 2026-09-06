father(amit,abhi).
mother(jaya,abhi).

father(abhi,aradh).
mother(aish,aradh).


parent(X,Y):-father(X,Y).
parent(X,Y):-mother(X,Y).


