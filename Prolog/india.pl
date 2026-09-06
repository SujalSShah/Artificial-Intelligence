% India Map Coloring using 3 colors: red, blue, green

coloring(JK, PB, RJ, UP, BH, WB, MP, MH) :-
    different(JK, PB),
    different(JK, RJ),
    different(PB, RJ),
    different(PB, UP),
    different(RJ, UP),
    different(RJ, MP),
    different(UP, BH),
    different(UP, MP),
    different(BH, WB),
    different(BH, MP),
    different(MP, MH),
    different(MH, WB).

% Define color differences
different(red, blue).
different(blue, red).
different(red, green).
different(green, red).
different(blue, green).
different(green, blue).
