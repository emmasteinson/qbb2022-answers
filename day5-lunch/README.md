#QBB- Lunch Exercise 3

Unix commands to get joined files with 

cut -d "," -f 5,6 aau1043_dnm.csv | sort | uniq -c > all_dnm.txt #cut out comma in aau1043_dnm.csv, cut 5th and 6th column which is ID and mother/father, sort and count number of unique proband ID occurences
grep father all_dnm.txt | cut -d "," -f1 > father_dnm.txt #make file with just father ID's and unique counts
grep mother all_dnm.txt | cut -d "," -f1 > mother_dnm.txt #make file with just mother ID's and unique counts

join -1 2 -2 2 father_dnm.txt mother_dnm.txt > joinedmf_dnm.txt #this joins father and mother files baed on second colum. my output joinedmf_dnm.txt has father in first column and mother in second column

cat aau1043_parental_age.csv | tr ',' ' ' > newparentalage.csv #this removes commas between columns and replaces with spaces


sort newparentalage.csv > sortedparentalage.csv #sort new parental age so you can join wiiiith joinedmf that has counts 


join -1 1 -2 1 joinedmf_dnm.txt sortedparentalage.csv > finaljoined.txt #this joins sorted age and count files 


#finaljoined.txt key 
proband id, father counts, mother counts, last two are father age, mother age


Exercise 2

3. Yes the relationship between maternal age and mutations is significant and for every year of age increase the number of mutations increases by .3776
4. Yes the relationship between paternal age and mutations is significant and for every  year of age increase the number of de novo mutations  increases by 1.35