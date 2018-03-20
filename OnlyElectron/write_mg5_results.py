from __future__ import print_function
import sys

if __name__ == '__main__':

    direc = "ScalarU_gUbmu-0/"

    outName = "print_results.txt"
    with open(outName, "w") as f:
        f.write("launch " + direc + " -i" + "\n")
        f.write("\tprint_results --path=./results.txt --format=short")
    print("Wrote", outName)
