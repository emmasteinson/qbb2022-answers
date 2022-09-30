Excellent work. You nailed needleman-wunsch and your alignment stats are (almost) exactly what I would have expected. There were two minor errors:

First, remember to initialize the first row and column of the traceback matrix, if you don't your program could run incorrectly if there are leading gaps (which is actually the case in the DNA alignment) (-0.5)

Secondly, your while condition is `i!=0 and j!=0`, but that will actually terminate as soon as either i or j become 0, which is not what we want if there are leading gaps. Because of this, your count for the number of gaps in the DNA alignment is slightly off (-0.25)

9.25/10
