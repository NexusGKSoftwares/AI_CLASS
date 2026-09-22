% ==============================================================================
% Lab 01: Symbolic AI, Knowledge Representation & Inference in Prolog
% Course: Introduction to Artificial Intelligence
% Associated Lectures: Lecture 01 (Laws of Thought) & Lecture 04 (Symbolic AI)
%
% Usage:
%   swipl -s labs/lab01_prolog_knowledge_base.pl
% ==============================================================================

% ------------------------------------------------------------------------------
% SECTION 1: Aristotelian Syllogism (Lecture 01)
% "All humans are mortal. Socrates is human. Therefore, Socrates is mortal."
% ------------------------------------------------------------------------------

human(socrates).
human(plato).
human(aristotle).
human(hypatia).

% Rule: If X is human, X is mortal.
mortal(X) :- human(X).


% ------------------------------------------------------------------------------
% SECTION 2: Family Tree & Recursive Relational Knowledge
% ------------------------------------------------------------------------------

% Facts: parent(Parent, Child)
parent(john, mary).
parent(john, david).
parent(sarah, mary).
parent(sarah, david).
parent(mary, alice).
parent(mary, bob).

male(john).
male(david).
male(bob).
female(sarah).
female(mary).
female(alice).

% Rules
father(F, C) :- parent(F, C), male(F).
mother(M, C) :- parent(M, C), female(M).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

grandparent(GP, GC) :-
    parent(GP, P),
    parent(P, GC).

% Recursive Ancestor Rule
ancestor(A, D) :- parent(A, D).
ancestor(A, D) :- parent(A, P), ancestor(P, D).


% ------------------------------------------------------------------------------
% SECTION 3: Symbolic Rule-Based Expert System (Medical Diagnostics)
% ------------------------------------------------------------------------------

% Patient Symptoms
symptom(alice, fever).
symptom(alice, cough).
symptom(alice, sore_throat).

symptom(bob, sneezing).
symptom(bob, runny_nose).

symptom(charlie, fever).
symptom(charlie, chills).
symptom(charlie, body_ache).
symptom(charlie, fatigue).

% Diagnostic Inference Rules
diagnose(Patient, flu) :-
    symptom(Patient, fever),
    symptom(Patient, chills),
    symptom(Patient, body_ache).

diagnose(Patient, common_cold) :-
    symptom(Patient, sneezing),
    symptom(Patient, runny_nose).

diagnose(Patient, pharyngitis) :-
    symptom(Patient, sore_throat),
    symptom(Patient, fever).


% ------------------------------------------------------------------------------
% SECTION 4: Interactive Helper Predicate
% ------------------------------------------------------------------------------

run_lab01 :-
    writeln('====================================================='),
    writeln('        Lab 01: Prolog Inference Demonstrations     '),
    writeln('====================================================='),
    writeln('1. Checking mortality of Socrates:'),
    (mortal(socrates) -> writeln('   -> Socrates is mortal! (Proven by Modus Ponens)') ; writeln('   -> Failed')),
    nl,
    writeln('2. Querying all descendants of John:'),
    forall(ancestor(john, Descendant), format('   -> Descendant: ~w~n', [Descendant])),
    nl,
    writeln('3. Running Medical Diagnostics Expert System:'),
    forall(diagnose(Patient, Disease), format('   -> Patient: ~w diagnosed with [~w]~n', [Patient, Disease])),
    writeln('=====================================================').
