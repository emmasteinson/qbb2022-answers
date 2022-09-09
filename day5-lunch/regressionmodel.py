#!/usr/bin/env python

import numpy as np 
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf 
from scipy import stats #special function for doing t-test
import statsmodels.api as sm

df = np.genfromtxt("finaljoined.txt", delimiter = ' ', dtype = None, encoding = None, names = "probandID, father_count, mother_count, father_age, mother_age")



#df = np.genfromtxt("finaljoined.txt", delimiter = ' ', dtype = None, encoding = None, names = True)

#print(df["probandID"])




#motherreg = smf.ols(formula = "mother_count ~ 1 + mother_age", data = df).fit() #does regression mother_age vs mother_count
#print(motherreg.summary())

fatherreg = smf.ols(formula = "father_count ~ 1 + father_age", data = df).fit() #does regression mother_age vs mother_count 

#run linear regression for father data
#print(fatherreg.summary())


#print(stats.ttest_ind(df["father_count"], df["mother_count"])) #ttest mother vs father count

new_data = df[0]
new_data.fill(0)
new_data['father_age'] = 50.5

print(fatherreg.predict(new_data))
#print(sm.stats.anova_lm(motherreg, fatherreg, typ = 1))


#fig, ax = plt.subplots()
#ax.hist(df["mother_count"], alpha = 0.5, label = "mother")
#ax.hist(df["father_count"], alpha = 0.5, label = "father")
#ax.set_xlabel("number of denove mutations")
#ax.set_ylabel("frequency")
#ax.legend()
#plt.savefig("ex2_c.png")







#to graph mother/father counts on scatter plot
#fig, ax = plt.subplots()
#ax.scatter(df["mother_age"], df["mother_count"])
#ax.set_xlabel("mother age")
#ax.set_ylabel("mother denovo mutation count")
#ax.set_title("mother denovo mutation count vs age")


#plt.xlim([0,60])
#plt.ylim([0,100])
#plt.savefig("ex2_a.png")
#plt.show()
#ax.legend()

