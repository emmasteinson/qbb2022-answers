#!/usr/bin/env python3

import sys # package that allows us to read in input from the command line (ex: name of vcf file)

def parse_vcf(fname): # defininng a function called parse_vcf and it takes an argument called "fname"
    vcf = [] # creates empty list called "vcf" (will be putting VCF info in here)
    info_description = {} # creating a dictionary 
    info_type = {} # creating a dictionary
    format_description = {} # creating a dictionary 
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        } # allows us to use information from the #header to tell python what data types to expect. dictionary because can store word and python associated 
    malformed = 0 #making variable that is counting number of lines in vcf that are badly formatted (have to initialize before forloop)
#trying to open VCF file; if it doesn't work, tell the user
    try: #use when doing something that might result in an error
        fs = open(fname) #creating a variable called fs, which is storing the opened vcf file 
    except: #this is what will happen if you get an error
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr) #error message to user

    for h, line in enumerate(fs): #loop thorugh every line in VCF file keeping track of the line number 
        if line.startswith("#"): #for header lines only 
            try:
                if line.startswith("##FORMAT"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            elif name == "Type":
                                Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        else: #if we are not on a header line, do this: 
            try: #try doing all of this:
                # fields is a list that stores the info in one line of the VCF
                fields = line.rstrip().split("\t") #a lot of data files have new line character at the end of every line. turns string into list. splits each line on tab character, so every column is a seperate item in the list. split turns string into list. takes line that is string, takes end character off and then turns into list deliminated by tabs. VCF files tab delim
                fields[1] = int(fields[1]) #converting SNP position into an integer (string before) (if this doesn't work we automatically go to "expect" block)
                if fields[5] != ".": #refers to QUAL column. if quality column is not empty (ex has decimanl in it that represents the SNP quality) 
                    fields[5] = float(fields[5]) #forcibly convert it to a decimal 
                info = {} # making a dictionary to store the information in the INFO column - the next bit of code is going to be about parsing the input column
                #we want info dictionary to look like this: {"AC" : 91, 
                                                            # "AN" : 5096
                                                            # ...,
                                                            # "NS" : 2548"}
                for entry in fields[7].split(";"): #8th column "INFO". "INFO" string looks like AC=91; AN=5096...converting string in 8th column into list. new list looks like ["AC=91", "AN=5096", ...] 
                    # the first entry we are working with is "AC=91"
                    temp = entry.split("=") # temp is a list. if we are working with "AC=91", temp = ["AC", "91"]
                    if len(temp) == 1: #if there's only one item in the temp list ("AC="): we want to update the dictionary so that we know that AC has no value for this SNP (length)
                        info[temp[0]] = None #temp[0] is "AC". we are adding info to the dictionary. we are adding "AC" : "None" (position 0 add none for position 1)
                        #dictionaries have keys and values. You can add info to a dictionary by doing dict_name[new_key] = new_value. Ex: info["AC"] = "91"
                    else: #otherwise info field is not empty and we are good
                        name, value = temp # temp is a list. temp = ["AC", "91"]. name = "AC" value = "91". another way to do it: name = temp[0]. value = temp[1] -name is first in temp value is second in temp
                        #next two lines converting the data in eaach entry to the correct data type. this data type was specified in the header section that we parsed above 
                        Type = info_type[name] # here, we are getting the name of the data type that the entry should be 
                        #Ex: type = info_type["AC"]. info_type is a dictionary we made in the header parsing section that tells us what data type that entry should be. 
                        info[name] = type_map[Type](value) #here we are getting the python function for converting the entry to the correct data type. 
                        # Ex: For AC: info["AC"] = type_map["Integer"]["91"]
                        #info ["AC"] = integer(91)
                fields[7] = info #replace 8th item of the fields list ie. list of columns in this line (INFO) with the info dicitonary we just made 
                if len(fields) > 8: # if we still have more columns after the INFO column, then we still have more stuff to do: 
                    # example of fields[8] (the FORMAAAT column) : "GT:DP:AF" format column normally seperated by : (hypothetical our file only has GT)
                    fields[8] = fields[8].split(":") #we are splitting the FORMAAT column by ":"
                                            #ex: "GT:DP:AF" -> ["GT", "DP", "AF"]
                    if len(fields[8]) > 1: #if there are multiple things in the format column we have to deal with all of them individually: 
                                                #FORMAT: GT:QV.  HG00097: 0|0:.3 
                        for i in range(9, len(fields)): # this goes through all the genotype columns after the FORMAT column -> for us, this is range(9, 2513)
                            fields[i] = fields[i].split(':') # split each genotype column along a ":"
                                                                    # 0|0:0.3 -> ["0|0", "0.3"]
                                                                   
                    else: #if the genotypes don't have more than ond value in them then we are good
                        fields[8] = fields[8][0] # fields[8] is ["GT"]
                                                # tthis code gets you  fields[8] = "GT"
                                                #we set teh value of fields[8] to be "GT" ( or the first item in our fields[8] list)
                 vcf.append(fields) #we finished reformatting and cleaning all of the columns now we add this line to our VCF list. the list is storing all the information from the VCF file
                 #fields is a list that contains the information fro the current line that we are working on. going through file line by line each fields deals with diff column
            except: #if anything in the tryblock fails, then: 
                malformed += 1 #increment the 'malformed' variable by 1
    #these next three lines are modifying the first line of the vcf list to match information from the headers
    vcf[0][7] = info_description 
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description
    #if there were any malformed lines, we are going to print out the number of lines so the user knows
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr)
    #at the very end of running the function, return the vcf list. give me the data back
    return vcf

# ignore all of this 
if __name__ == "__main__":
    fname = sys.argv[1]
    vcf = parse_vcf(fname)
    for i in range(10):
        print(vcf[i])
