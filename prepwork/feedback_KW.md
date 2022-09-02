This script is very good! Good use of google to figure things out and great job commenting your script, including your pseudocode.
  * The list comprehension setting up the list of lines is very nice
  * subsetting the list to only be the last 10 lines is good.
  * Finally, it prints every line from the subset successfully.

Instead of the current way you subset your list of lines, I would recommend using `my_list_sub = my_list[-n_lines:]` so that it subsets however many of the last lines the user specified (or the default if nothing was specified). As written, it will only subset and print the last 10 lines.
