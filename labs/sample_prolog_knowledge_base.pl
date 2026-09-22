% ==============================================================================
% Sample Prolog Knowledge Base: Syllogisms & Logic (Lecture 01 & 04)
% Run with: swipl -s labs/sample_prolog_knowledge_base.pl
% ==============================================================================

% Facts
man(socrates).
man(plato).
man(aristotle).

philosopher(socrates).
philosopher(plato).
philosopher(aristotle).

% Rules (Deductive Reasoning: All men are mortal)
mortal(X) :- man(X).

% Rules: Mentorship relations
mentor(socrates, plato).
mentor(plato, aristotle).

% Transitive teacher rule
ancestor_mentor(X, Y) :- mentor(X, Y).
ancestor_mentor(X, Y) :- mentor(X, Z), ancestor_mentor(Z, Y).
