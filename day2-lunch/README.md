# QBB2022 -Day 2 - Lunch Exercises Submission 


Create a copy of the script we produced during the live-coding lecture, /Users/cmdb/cmdb-quantbio/assignments/bootcamp/extend_bed_parser/slides_asynchronous_or_livecoding_resources/bed_parser.py. This will serve as your starting point for the assignment. In the interactive lecture, if we could not correctly convert data within a line to the expected data types, then the line was malformed. Now you are going to extend this parser to check for several other conditions in addition to successful data type conversion.

    Check that the number of fields is appropriate. Your script should allow for files with bed3, bed4, bed5, bed6, bed7, bed8, bed9, and bed12 formatting, but not lines that follow bed10 and bed11 formatting as these entries are prohibited

#!/usr/bin/env python3
```
import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, float, str, int, int, str, int, str, str] #set field types
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if fieldN < 3 or fieldN ==10 or fieldN ==11: #set error to appear if field number is 3 10, or 11
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue
        try:
            for j in range(min(len(field_types), len(fields))):
                fields[j] = field_types[j](fields[j])
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
    fs.close()
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
```