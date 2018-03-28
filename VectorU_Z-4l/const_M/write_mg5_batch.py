from __future__ import print_function
import sys

if __name__ == '__main__':

    MU = int(sys.argv[1])
    MU_str = "_MU-"+str(MU).zfill(2)

    g_vec = [.01, .02, .05, .1, .15, .2, .25, .3, .35, .4, .45, .5, .6, .7]
    g_min, g_max = g_vec[0], g_vec[-1]
    g_str = "_g-" + format(g_min, ".2f")[1::] + "to" + format(g_max, ".2f")[1::]

    outName = "scan" + MU_str + g_str + ".txt"
    outFile = open(outName, "w")

    for g in g_vec:
        gUbe, gUbmu = g, g
        run_tag = MU_str[1::] + "_g-" + format(g, ".2f")[1::]
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
