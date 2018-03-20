from __future__ import print_function
import sys

if __name__ == '__main__':

    MU, gUbe, gUbmu = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    run_tag = "MU-" + str(MU).zfill(2) + "_gUbe-" + format(gUbe, ".2f")[1::]
    outName = "mg5_run.txt"
    with open(outName, "w") as f:
        f.write("generate_events" + "\n")
        f.write("Cards/param_card_default.dat" + "\n")
        f.write("set MUb " + str(MU) + "\n")
        f.write("set gUbe " + str(gUbe) + "\n")
        f.write("set gUbmu " + str(gUbmu) + "\n")
        f.write("set run_tag " + run_tag  + "\n")
    print("Wrote", outName)
