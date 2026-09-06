% ------------ FACTS ------------

% Gender
male(john).
male(mike).
male(paul).
male(steve).
male(bob).

female(mary).
female(lisa).
female(susan).
female(anna).
female(kate).

% Parent relationships
parent(john, mike).
parent(mary, mike).

parent(john, lisa).
parent(mary, lisa).

parent(mike, steve).
parent(susan, steve).

parent(mike, anna).
parent(susan, anna).

parent(paul, bob).
parent(lisa, bob).

% ------------ RULES ------------

% Father: male and parent
father(X, Y) :- male(X), parent(X, Y).

% Mother: female and parent
mother(X, Y) :- female(X), parent(X, Y).

% Grandfather: male and parent of a parent
grandfather(X, Y) :- male(X), parent(X, Z), parent(Z, Y).

% Grandmother: female and parent of a parent
grandmother(X, Y) :- female(X), parent(X, Z), parent(Z, Y).

% Sibling: share at least one parent
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Brother: male sibling
brother(X, Y) :- male(X), sibling(X, Y).

% Sister: female sibling
sister(X, Y) :- female(X), sibling(X, Y).

% Uncle: male sibling of a parent
uncle(X, Y) :- male(X), sibling(X, Z), parent(Z, Y).

% Aunt: female sibling of a parent
aunt(X, Y) :- female(X), sibling(X, Z), parent(Z, Y).

% Nephew: male child of a sibling
nephew(X, Y) :- male(X), parent(Z, X), sibling(Z, Y).

% Niece: female child of a sibling
niece(X, Y) :- female(X), parent(Z, X), sibling(Z, Y).

% Cousin: children of siblings
cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B).

% Relative (demonstrates disjunction usage)
relative(X, Y) :-
    father(X, Y);
    mother(X, Y);
    brother(X, Y);
    sister(X, Y);
    uncle(X, Y);
    aunt(X, Y);
    cousin(X, Y).
