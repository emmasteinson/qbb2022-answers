#!/usr/bin/env python
import sys

import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors   
    # in1_fname should be ddCTCF
    # in2_fname should be dCTCF
    # bin_fname should be bed file with bin locations
    
in1_fname, in2_fname, bin_fname, out_fname = sys.argv[1:5]
data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
    ('F1', int), ('F2', int), ('score', float)]))
data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([
    ('F1', int), ('F2', int), ('score', float)]))
frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
    ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

chrom = b'chr15'
start = 11170245
end = 12070245
start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                     (frags['start'] <= start) &
                                     (frags['end'] > start))[0][0]]
end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                   (frags['start'] <= end) &
                                   (frags['end'] > end))[0][0]] + 1 

def filter_data(data1):
    #pull out the binds within the desired range
    col1 = data1['F1']
    col2 = data1['F2']
    rows = (col1 >= start_bin) & (col2 < end_bin)
    data1 = data1[numpy.where(rows)]

    #log transform the scores
    logged = numpy.log2(data1['score'])
    data1['score'] = logged #log transfoorm the score

    minscore = numpy.amin(data1['score']) #set them in score as a vaariable
    newscore = data1['score'] - minscore #subtract the min score from all score values so min is 0
    data1['score'] = newscore #overwrite data1

    #print(data1['score'][0])
    #print(data1['score'][0][0])

    lendata = len(data1['score'])
    mat1 = numpy.zeros((end_bin - start_bin +1, end_bin - start_bin+1))
    #print(mat1)
    # print(data1['score'][0][0])

    for i in range(lendata):
        # score_col = data1['score'][0]
        score = data1['score'][i] #score_col[i]
        x_cord = data1['F1'][i] - start_bin
        y_cord = data1['F2'][i] - start_bin
    #print(y_cord)
        mat1[x_cord, y_cord] = score
        mat1[y_cord, x_cord] = score
    return(mat1)

mat1 = filter_data(data1)
mat2 = filter_data(data2)

#functions for subtraction matrix
def remove_dd_bg(mat):
    N = mat.shape[0]
    mat2 = numpy.copy(mat)
    for i in range(N):
        bg = numpy.mean(mat[numpy.arange(i, N), numpy.arange(N - i)])
        mat2[numpy.arange(i, N), numpy.arange(N - i)] -= bg
        if i > 0:
            mat2[numpy.arange(N - i), numpy.arange(i, N)] -= bg
    return mat2
ddmat1 = remove_dd_bg(mat1)
ddmat2 = remove_dd_bg(mat2)

def smooth_matrix(mat):
    N = mat.shape[0]
    invalid = numpy.where(mat[1:-1, 1:-1] == 0)
    nmat = numpy.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat
smoothmat1 = smooth_matrix(ddmat1)
smoothmat2 = smooth_matrix(ddmat2)

submat = smoothmat2 - smoothmat1

#plot

fig, ax = plt.subplots(ncols = 1, nrows = 3)

#set matrices so they have the same maximum
max1 = numpy.amax(mat1)
max2 = numpy.amax(mat2)
absmax = max(max1, max2) 


ax[0].imshow(mat1, cmap = "magma", vmax = absmax)
ax[0].set_title("ddCTF matrix")
ax[1].imshow(mat2, cmap = "magma", vmax = absmax)
ax[1].set_title("dCTF matrix")
ax[2].imshow(submat, cmap = "magma")
ax[2].set_title("subtraction matrix")

plt.tight_layout()
fig.savefig("HiC-plotsfulls.png")
plt.show()
