#!/usr/bin/env python
import sys
import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors
in1_fname, bin_fname, out_fname = sys.argv[1:4]
data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
    ('F1', int), ('F2', int), ('score', float)]))
frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
    ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))
print(data1)
chrom = b'chr15'
start = 10400000
end = 13400000
start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                     (frags['start'] <= start) &
                                     (frags['end'] > start))[0][0]]
end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                   (frags['start'] <= end) &
                                   (frags['end'] > end))[0][0]] + 1
print(start_bin, end_bin)
def filtered_data(data1):
    col1 = data1["F1"]
    col2 = data1["F2"]
    rows = (col1 >= start_bin) & (data1["F2"] <= end_bin)
    data1 = data1[numpy.where(rows)]
    logged = numpy.log2(data1["score"])
    data1["score"] = logged
    print(data1["score"])
    minimum = numpy.amin(data1["score"])
    data1["score"] = data1["score"] - minimum
    lendata = len(data1["score"])
    mat1 = numpy.zeros((end_bin - start_bin, end_bin - start_bin))
    for i in range(lendata):
        score = data1["score"][i]
        xcoord = data1["F1"][i] - start_bin
        ycoord = data1["F2"][i] - start_bin
        mat1[xcoord, ycoord] = score
        mat1[ycoord, xcoord] = score
    return(mat1)
mat = filtered_data(data1)
insulationlist = []
ntlist = []
for i in range(len(mat)):
    insulation_score = numpy.mean(mat[(i - 5):i, i:(i + 5)])
    insulationlist.append(insulation_score)
ntlist = numpy.linspace(10400000, 13400000, len(insulationlist))

fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
ax[0].axis('off')
plt.margins(x=0)
ax[1].set_xlim(10400000, 13400000)
plt.subplots_adjust(left=0.15,
                bottom=0.1,
                right=1.0,
                top=1.0,
                wspace=0.4,
                hspace=0.0)
ax[0].imshow(mat, cmap = "magma")

ax[1].plot(ntlist, insulationlist)

ax[1].set_xlabel("Region")
ax[1].set_ylabel("Insulator Score")
plt.tight_layout()
plt.show()
fig.savefig("Insulator.png")