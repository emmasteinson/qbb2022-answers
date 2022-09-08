# day 4 homework feedback

The plots look great overall! I'd recommend using the `xticklabels` and `yticklabels` arguments/options in `sns.heatmap` to set the ticklabels to be equal to the number of tosses and probability of heads arrays so that you can directly see in the plot the simulation parameter combo that led to each power. (rather than using the "auto" argument)

While you've submitted both plots, I only see code making one of the plots. please update the code. However, overall the code looks fantastic and directly edits the `run_experiment()` function like requested beautifully! Good work!

Comments in your README -- fantastic comments and observations overall. Specifically with regards to the comment "The number of iterations in our simulation corresponds to the nubmber of donors (?)." -- the number of iterations in our simulation (100) corresponds to the number of independent simulations -- "The power for each study design was computed from 1000 independent
simulations.", according to the caption.
