from __future__ import print_function
import sys

if __name__ == '__main__':

    gUbmu = float(sys.argv[1])
    gUbe = float(sys.argv[1])
    g_str = "_g-" + format(gUbe, ".2f")[1::]

    MU_vec = [5, 6, 8, 10, 15, 18, 20, 25, 30, 35, 40, 50, 60, 70]
    MU_min, MU_max = MU_vec[0], MU_vec[-1]
    MU_str = "_MU-"+str(MU_min).zfill(2) + "to" + str(MU_max).zfill(2)

    outName = "scan" + MU_str + g_str + ".txt"
    outFile = open(outName, "w")

    for MU in MU_vec:
        run_tag = "MU-" + str(MU).zfill(2) + g_str
        outFile.write("generate_events" + "\n")
        outFile.write("\t" + "./Cards/param_card_default.dat" + "\n")
        outFile.write("\tset gUbe " + str(gUbe) + "\n")
        outFile.write("\tset gUbmu " + str(gUbmu) + "\n")
        outFile.write("\tset MUb " + str(MU) + "\n")
        outFile.write("\tset WUb Auto" + "\n")
        outFile.write("\tset run_tag " + run_tag + "\n")

#   outFile.write("launch " + direc + " -i" + "\n")
#   outFile.write("print_results --path=./results.txt --format=short")

    outFile.close()
    print("Wrote", outName)
