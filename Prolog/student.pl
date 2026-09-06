% Facts
boy(niraj).
boy(manoj).
girl(lata).
girl(asha).
girl(usha).

% Rules
student(X):-boy(X).
student(X):-girl(X).
