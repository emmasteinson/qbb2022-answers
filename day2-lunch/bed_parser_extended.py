#!/usr/bin/env python

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
        
    bed = [] #every item in list will be line in bed file which is basically region in the              genome
    field_types = [str, int, int, str, float, str, int, int]
    
    # create a counter for malformed lines
    malformed = 0 #creates counter for malformed lines
    
    for i, line in enumerate(fs):
        # skipping headers
        if line.startswith("#"):
            continue
        # converting `lines' into a list called `fields`
        fields = line.rstrip().split()
        # creating fieldN, which stores the number of columns we have
        fieldN = len(fields)
        
        # this checks is fields are less than or equal to 10 or 11 and complains if this is the case
        if fieldN < 3 or fieldN == 10 or fieldN == 11:
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue
        
        try:
            # for files that have 9 columns verify that there are 3 integers for itemRGB (the 9th column)
            # make sure the file we're working with has at least 9 columns
            if fieldN >= 9: #if we have atleast 9 columns
                # pull out the 9th column
                rgb = fields[8]
                # convert column into list
                rgb_list = rgb.split(',') # rgb_list looks like: ["254", "0", "0"]
                # convert every item into an integer
                for i, item in enumerate(rgb_list): #have to iterate through rgb_list to                   convert to integers. need position and integer
                    #i:0
                    #item: 254
                    #rgb_list[0] = int ("254") -> rgb_list[0] = 254
                    rgb_list[i] = int(item) #converts items in list to integer
                    #rgb_list  looks like [254, 0, 0]
                # rgb_list = [int(item) for item in rgb_list]
                # replace the 9th column with our list
                fields[8] = rgb_list

            # only do this for files that have 12 columns
            if fieldN == 12:
                # strip the extra comma from blockSizes (column 11) and blockStarts (column 12)
                # convert column 11 and 12 into a list
                blockSizes = fields[10].rstrip(",").split(",") #convert column 12
                 
                blockStarts = fields[11].rstrip(",").split(",") #convert column 11
                # blockSizes looks like: ["76", "140", "86", "211"]
                # blockStarts looks like: ["0", "749", "2587", "5136"]

                # Convert items in blockSizes to integers
                for i, item in enumerate(blockSizes):
                    blockSizes[i] = int(item)
                # replace the 11th column with our converted list
                fields[10] = blockSizes

                # Convert items within blockStarts to integers
                for i, item in enumerate(blockStarts):
                    blockStarts[i] = int(item)
                # replace the 12th column with our converted list
                fields[11] = blockStarts

                # check that blockSizes and blockStarts length matches blockCount (column 10)
            
                blockCount = int(fields[9]) #pull out value of blockCount
                # check that length of blockSizes and blockStarts == blockCount
                if len(blockStarts) != blockCount: #if not equal
                    # increment our counter of malformed lines
                    malformed += 1
                if len(blockSizes) != blockCount:
                    # increment our counter of malformed lines
                    malformed += 1
                # replace 10th column with its integer version
                fields[9] = blockCount
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
                
        # convert rest of columns to the correct data type (not 9-12)
        try:
            for j in range(min(len(field_types), len(fields))):
                fields[j] = field_types[j](fields[j])
            # if data type conversion works append this correct line to the bed list
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
                   
    fs.close()
    print(malformed)
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)