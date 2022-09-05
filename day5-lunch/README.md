#QBB- Lunch Exercise 3

Exercise 1

Unix commands to get joined files:

cut -d "," -f 5,6 aau1043_dnm.csv | sort | uniq -c > all_dnm.txt #cut out comma in aau1043_dnm.csv, cut 5th and 6th column which is ID and mother/father, sort and count number of unique proband ID occurences

grep father all_dnm.txt | cut -d "," -f1 > father_dnm.txt #make file with just father ID's and unique counts

grep mother all_dnm.txt | cut -d "," -f1 > mother_dnm.txt #make file with just mother ID's and unique counts

join -1 2 -2 2 father_dnm.txt mother_dnm.txt > joinedmf_dnm.txt #this joins father and mother files baed on second colum. my output joinedmf_dnm.txt has father in first column and mother in second column

cat aau1043_parental_age.csv | tr ',' ' ' > newparentalage.csv #this removes commas between columns and replaces with spaces


sort newparentalage.csv > sortedparentalage.csv #sort new parental age so you can join with joinedmf_dnm.txt that has counts 


join -1 1 -2 1 joinedmf_dnm.txt sortedparentalage.csv > finaljoined.txt #this joins sorted age and count files 


finaljoined.txt key: 
proband id, father counts, mother counts, father age, mother age


Exercise 2
1. Use numpy genfromtxt to load joined data

df = np.genfromtxt("finaljoined.txt", delimiter = ' ', dtype = None, encoding = None, names = "probandID, father_count, mother_count, father_age, mother_age")

2. Use matplot lib to plot denovo mutations vs age for maternal and paternal

fig, ax = plt.subplots()
ax.scatter(df["parent_age"], df["parent_count"])
ax.set_xlabel("parent age")
ax.set_ylabel("parent denovo mutation count")
ax.set_title("parent denovo mutation count vs age")


3. Yes the relationship between maternal age and mutations is significant and for every year of age increase the number of mutations increases by .3776

motherreg = smf.ols(formula = "mother_count ~ 1 + mother_age", data = df).fit() 
print(motherreg.summary())


4. Yes the relationship between paternal age and mutations is significant and for every  year of age increase the number of de novo mutations increases by 1.35

fatherreg = smf.ols(formula = "father_count ~ 1 + father_age", data = df).fit()
print(fatherreg.summary())


6. Yes the difference is significant between maternally inherited de novo mutations per proband is significantly different than the number of paternally inherited de novo mutations. T-test results in a very small p-value 2.198603179308129e-264

print(stats.ttest_ind(df["father_count"], df["mother_count"]))

7. The number of mutations for a proband with a father who was 50.5 years old at the proband's birth is 78.018535 de novo mutations.

new_data = df[0]
new_data.fill(0)
new_data['father_age'] = 50.5
print(fatherreg.predict(new_data))
