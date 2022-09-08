#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )


fig, ax = plt.subplots()
plt.yscale('log') #make y-scale log
ax.set_ylabel("frequency")
ax.set_xlabel("allele count")
ax.hist( ac, density=True )
fig.savefig( vcf + ".png" )
plt.title(vcf) #make title vcf
plt.show() #show plot



fs.close()

