from __future__ import print_function
import sys

if __name__ == '__main__':

    MU_min, MU_max, MU_inc = 1, 90, 10
    g = float(sys.argv[1])
    g_str = "_g-" + format(g, ".2f")[1::]
    direc = "ScalarU_pp-Z-4l_exclusion/"

    outName = "scan_MU-"+str(MU_min).zfill(2)+"to"+str(MU_max)+g_str+".txt"
    outFile = open(outName, "w")

    MU_vec = range(0, MU_max + MU_min, MU_inc)
    MU_vec[0] = MU_vec[0] + MU_min;

    for MU in MU_vec:
        run_tag = "MU-" + str(MU).zfill(2) + g_str
        outFile.write("launch " + direc + "\n")
        outFile.write("\t" + direc+"Cards/param_card_default.dat" + "\n")
        outFile.write("\tset gUB " + str(g) + "\n")
        outFile.write("\tset MUb " + str(MU) + "\n")
        outFile.write("\tset WUb Auto" + "\n")
        outFile.write("\tset run_tag " + run_tag + "\n")

    outFile.write("launch " + direc + " -i" + "\n")
    outFile.write("\tprint_results --path=./"+direc+"results.txt --format=short")

    outFile.close()
    print("Wrote", outName)
