# for ONE bin file

# getting the names of all the contigs in the bin file of interest
contigs=$(grep ">" ../READS/bins_dir/bin.6.fa | cut -f 2 -d ">")

echo $contigs

# loop through all the contigs
for id in $contigs
do
	# pull out the kraken classification for that contig ID
	# and put it into a file for that bin
	grep $id assembly.kraken >> bin6.kraken
done

# convert the kraken file into kronatools format
./kraken.py bin6.kraken bin6

# run ktImportText on all your krona files
ktImportText -q bin1_krona.txt bin2_krona.txt bin3_krona.txt bin4_krona.txt bin5_krona.txt bin6_krona.txt -o bins.html










