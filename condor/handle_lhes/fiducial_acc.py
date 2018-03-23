from __future__ import print_function
from __future__ import division
import sys
import ROOT as rt
import math
from array import array
from LHEevent import *
from LHEfile import *
import plotTools

if __name__ == '__main__':

    ################
    #  PARAMETERS  #
    ################

    MZ = 91.2
    cutMll = cutM4l = cutMZ1 = cutEta = cutPt1 = cutPt2 = cutPt34 = True



    ################
    #  INITIALIZE  #
    ################

    PT1_MIN, PT2_MIN, PT34_MIN = 20, 10, 5
    ETA_MAX, MLL_MIN = 2.5, 4
    MZ1_MIN = 40
    M4L_MIN, M4L_MAX = 80, 100

    n_gen = n_acc = 0
    n_SM = n_NP = n_SM_acc = n_NP_acc = 0
    n_Mll = n_M4l = n_MZ1 = n_eta = n_pT1 = n_pT2 = n_pT34 = 0



    ################
    #  GET EVENTS  #
    ################

    inFile = sys.argv[1]
    tag = inFile[0:5]
    myLHEfile = LHEfile(inFile)
    myLHEfile.setMax(100000)
    eventsReadIn = myLHEfile.readEvents()
    for oneEvent in eventsReadIn:
        myLHEevent = LHEevent()
        myLHEevent.fillEvent(oneEvent)
        passM4l, accepted = False, True
        n_Z = n_U = 0
        e_lv, e_id, e_q = [], [], []
        mu_lv, mu_id, mu_q = [], [], []

        # Sort particles
        n_gen += 1
        for i in range(0, len(myLHEevent.Particles)):
            p = myLHEevent.Particles[i]
            if abs(p['ID']) == 23:
                n_Z += 1
            elif abs(p['ID']) == 99:
                n_U += 1
            elif abs(p['ID']) == 11: 
                e_lv.append(rt.TLorentzVector(p['Px'], p['Py'], p['Pz'], p['E']))
                e_id.append(abs(p['ID']))
                e_q.append(math.copysign(1, p['ID']))
            elif abs(p['ID']) == 13:
                mu_lv.append(rt.TLorentzVector(p['Px'], p['Py'], p['Pz'], p['E']))
                mu_id.append(abs(p['ID']))
                mu_q.append(math.copysign(1, p['ID']))
        n_e, n_mu = len(e_lv), len(mu_lv)

        # Sort leptons by pT
        l_lv, l_id, l_q = e_lv + mu_lv, e_id + mu_id, e_q + mu_q
        n_l = len(l_lv)
        l_group = [(l_lv[i].Pt(), l_id[i], l_q[i]) for i in range(len(l_lv))]
        l_group.sort(reverse = True)
        l_id = [ID for (pT, ID, Q) in l_group]
        l_q = [Q for (pT, ID, Q) in l_group]
        l_lv.sort(key = rt.TLorentzVector.Pt, reverse = True)



        ################
        #  APPLY CUTS  #
        ################

        # Mll for opposite-charge leptons of same flavor
        if cutMll:
            for i in range(n_e):
                for j in range(i):
                    if (e_q[i] * e_q[j] < 0 and (e_lv[i] + e_lv[j]).M() < MLL_MIN):
                        accepted = False
            for i in range(n_mu):
                for j in range(i):
                    if (mu_q[i] * mu_q[j] < 0 and (mu_lv[i] + mu_lv[j]).M() < MLL_MIN):
                        accepted = False
            if accepted:
                n_Mll += 1
        elif len(tag) < 7:
            tag = tag + "_no-Mll"

        # M4l in Z mass window
        if cutM4l:
            M4l = (l_lv[0] + l_lv[1] + l_lv[2] + l_lv[3]).M()
            if not (M4L_MIN < M4l < M4L_MAX):
                accepted = False
            if accepted:
                n_M4l += 1
                passM4l = True
        elif len(tag) < 7:
            tag = tag + "_no-M4l"

        # MZ1 for pair closest to Z mass
        if cutMZ1:
            MZ1 = 0
            for i in range(n_e):
                for j in range(i):
                    Mll = (e_lv[i] + e_lv[j]).M()
                    if (e_q[i] * e_q[j] < 0 and abs(Mll - MZ) < abs(MZ1 - MZ)):
                        MZ1 = Mll
            for i in range(n_mu):
                for j in range(i):
                    Mll = (mu_lv[i] + mu_lv[j]).M()
                    if (mu_q[i] * mu_q[j] < 0 and abs(Mll - MZ) < abs(MZ1 - MZ)):
                        MZ1 = Mll
            if MZ1 < MZ1_MIN:
                accepted = False
            if accepted:
                n_MZ1 += 1
        elif len(tag) < 7:
            tag = tag + "_no-MZ1"

        # Maximum eta
        if cutEta:
            for i in range(n_l):
                if abs(l_lv[i].Eta()) > ETA_MAX:
                    accepted = False
            if accepted:
                n_eta += 1
        elif len(tag) < 7:
            tag = tag + "_no-eta"

        # Leading lepton pT
        if cutPt1:
            if l_lv[0].Pt() < PT1_MIN:
                accepted = False
            if accepted:
                n_pT1 += 1
        elif len(tag) < 7:
            tag = tag + "_no-pT1"

        # Subleading lepton pT
        if cutPt2:
            if l_lv[1].Pt() < PT2_MIN:
                accepted = False
            if accepted:
                n_pT2 += 1
        elif len(tag) < 7:
            tag = tag + "_no-pT2"

        # Absolute minimum pT for flavors
        if cutPt34:
            if (l_lv[2].Pt() < PT34_MIN or l_lv[3].Pt() < PT34_MIN):
                accepted = False
            if accepted:
                n_pT34 += 1
        elif len(tag) < 7:
            tag = tag + "_no-pT34"

        # Total accepted events
        if accepted:
            n_acc += 1



    ################
    #    OUTPUT    #
    ################

    # Print acceptance
#   print(n_Mll, n_M4l, n_MZ1, n_eta, n_pT1, n_pT2, n_pT34, n_acc)
    print(n_M4l, n_acc)
