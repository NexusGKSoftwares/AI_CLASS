% --- FACTS ---
% parent(Parent, Child)
parent(john, mary).
parent(john, tom).
parent(susan, mary).
parent(susan, tom).
parent(mary, alice).
parent(tom, bob).

% Gender facts
male(john).
male(tom).
male(bob).

female(susan).
female(mary).
female(alice).

% --- RULES ---
% A person is a father if they are male and a parent
father(X, Y) :- parent(X, Y), male(X).

% A person is a mother if they are female and a parent
mother(X, Y) :- parent(X, Y), female(X).

% A grandparent is a parent of a parent
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% Two people are siblings if they share a parent and are not the same person
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.

% Two people are cousins if their parents are siblings
cousin(X, Y) :- parent(P1, X), parent(P2, Y), sibling(P1, P2).