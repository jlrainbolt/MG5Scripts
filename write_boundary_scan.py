from __future__ import print_function
import sys

if __name__ == '__main__':

    inFile = sys.argv[1]
    with open(inFile, "r") as f:
        data = f.readlines()
        data = data[1::]

    MU_vec, g_vec = [], []
    for line in data:
        [MU, g] = line.split()
        MU_vec.append(MU)
        g_vec.append(g)
    direc = "ScalarU_pp-Z-4l_exclusion/"

    outName = "scan_" + inFile
    outFile = open(outName, "w")

    for i in range(len(data)):
        MU, g = MU_vec[i], g_vec[i]
        run_tag = "MU-" + MU + "_g-" + g
        outFile.write("launch " + direc + "\n")
        outFile.write("\t" + direc+"Cards/param_card_default.dat" + "\n")
        outFile.write("\tset gUB " + g + "\n")
        outFile.write("\tset MUb " + MU + "\n")
        outFile.write("\tset WUb Auto" + "\n")
        outFile.write("\tset run_tag " + run_tag + "\n")

    outFile.write("launch " + direc + " -i" + "\n")
    outFile.write("\tprint_results --path=./"+direc+"results.txt --format=short")

    outFile.close()
    print("Wrote", outName)
