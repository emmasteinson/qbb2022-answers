#USAGE: python scriptname.py input_filename number_lines_to_display
import sys #import module
filename = sys.argv[1] #set input file
if len(sys.argv) > 2: #IF user specified number of lines
    n_lines = int(sys.argv[2]) #THEn set the desired number of lines
else: #OTHERWISE
    n_lines = 10 #THEN set lines to 10
with open(filename) as x: #SET file as variable
	my_list = [line for line in x] #add lines to storage list
my_list_sub = my_list[-10:-1] #SET sub list to be last 10 lines
for line in my_list_sub: #FOR every line in sublist list
	    print(line.strip('\r\n')) #PRINT