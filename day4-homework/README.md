#QBB-Day4 Homework

Part A
```
numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1] 
```
this line is setting the range of the probabilities of the unfair coin to return heads as between .55 and 1.05 (but not including 1.05) each time through the simulation with a step size of .05 (first time through p = .55, next time through p=.6 until p = 1.0). np.around is evenly ronding to two decimals so the matrix is easier to view. The [::-1] indicates that the list of probabilities is being iterated through backwards. 

Part C

The heatmap demonstrates that power is higher the more tosses you do and the more and the more the probability of getting heads deviates from .5. This makes sense as you are more likely to be able to capture deviations from binomial expectations the more times you preform the experiment and the more "rigged" it is. ***my heat map x and y labels aren't right I am struggling to fix
 
Part D

This study is testing whether there are alleles that violate Mendel's Law of Segregation and whether there are rigged alleles that are disproportionately transmitted to the next generation. The study used single cell sequencing from sperm to test whether meosis maintains balanced transmission of alleles to the gamete pool. It is similar to our coin toss simulation in that the transmission rate axis corressponds to our probability of getting heads axis and the number of cells corresponds to the number of tosses in our experiment. The number of iterations in our simulation corresponds to the nubmber of donors (?). These simulations use a binomial test because under "normal" expected circustances there is a 50-50 chance of getting heads or tails and there is a 50-50 chance of an allele being transmitted to the next generation. To elaborate, each outcome can be classified as a success or failure and there is the same probabilitty of success (allele transmission or heads) on each trial. 

