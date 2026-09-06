associative_law(A, B, C, R1) :-
    R1 is (A + B) + C,
associative_law(A, B, C, R2) :-
    R2 is A + (B + C).
