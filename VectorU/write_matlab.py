from __future__ import print_function
from __future__ import division
import sys
import numpy as np

# Input parameters
B_95, B_90, B_68 = 4.97087, 4.8769, 4.66639
B_SM, B_SM_unc = 4.54542, 0.258653
cross_SM, error_SM = 0.310212484609, 0.000265461345335
n_M4l_SM, n_acc_SM = 62952, 6605


# Read in file
MU_vec, g_vec = [], []

filename = sys.argv[1]
with open(filename, "r") as f:
    data = f.readlines()
    data = data[1::]

for line in data:
    [MU, g, cross, error, n_M4l, n_acc] = line.split()
    if not MU in MU_vec:
        MU_vec.append(MU)
    if not g in g_vec:
        g_vec.append(g)

MU_len, g_len = len(MU_vec), len(g_vec)
MU_vec, g_vec = sorted(MU_vec), sorted(g_vec)
MU_dict = dict(zip(MU_vec, range(MU_len)))
g_dict = dict(zip(g_vec, range(g_len)))
cross_mat = np.zeros((g_len, MU_len))
n_M4l_mat = np.zeros((g_len, MU_len))
n_acc_mat = np.zeros((g_len, MU_len))

for line in data:
    [MU, g, cross, error, n_M4l, n_acc] = line.split()
    cross_val, error_val = float(cross), float(error)
    n_M4l_val, n_acc_val = int(n_M4l), int(n_acc)
   
    cross_mat[g_dict[g], MU_dict[MU]] = cross_val
    n_M4l_mat[g_dict[g], MU_dict[MU]] = n_M4l_val
    n_acc_mat[g_dict[g], MU_dict[MU]] = n_acc_val

with open("data.m", "w+b") as f:
    f.write("B_95 = "+str(B_95)+"; ")
    f.write("B_90 = "+str(B_90)+"; ")
    f.write("B_68 = "+str(B_68)+";\n")

    f.write("B_SM = "+str(B_SM)+"; ")
    f.write("cross_SM = "+str(cross_SM)+";\n")
    
    f.write("n_M4l_SM = "+str(n_M4l_SM)+"; ")
    f.write("n_acc_SM = "+str(n_acc_SM)+";\n\n")

    f.write("MU = [")
    for i in range(MU_len):
        f.write(str(MU_vec[i])+" ")
    f.write("];\n")
    f.write("g = [")
    for j in range(g_len):
        f.write(str(g_vec[j])+" ")
    f.write("]';\n\n")

    f.write("cross = [")
    np.savetxt(f, cross_mat, fmt='%.12f', newline='\n    ')
    f.write("];\n\n")

    f.write("n_M4l = [")
    np.savetxt(f, n_M4l_mat, fmt='%i', newline='\n    ')
    f.write("];\n\n")

    f.write("n_acc = [")
    np.savetxt(f, n_acc_mat, fmt='%i', newline='\n    ')
    f.write("];\n\n")

