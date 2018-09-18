import os, sys, time

class FEWZInputGenerator:
    def __init__( self ):

        self.tag = ""
        self.FEWZBinPath = ""
        self.nCore = 0
        # -- follow the order in FEWZ parameter card
        # -- put default values first
        # -- but some variables should be defined before running
        # -- They will be detected in CheckMandatoryOptions() if one of them is not set
        self.Energy = 13000
        
        self.muF = 9999
        self.muR = 9999
        self.scaleVarBy2 = 0 # -- 1: include the cale variation by factor 2 (mu*1/2, mu*2)

        self.alpha0Photon = 0 # -- for PI contribution -- #
        self.alphaEff = 0.007756146746

        self.leptonMass = 0.10565837 # -- muon

        # -- 1 = Gmu scheme / 2 = alphaMz scheme / 3 = alpha0 scheme
        self.inputScheme = 1

        # -- in %
        self.relUnc = 0.0
        self.absUnc = 0.0 # -- Menual: "It is recommended the user rely on the absolute accuracy" (by gussing rel.unc. using NLO x-section)
        self.nCall = 1000000
        self.nIncreasedCall = 500000
        self.maxNEval = 200000000
        self.randomSeed = 11

        # -- 0 = LO / 1 = NLO / 2 = NNLO
        self.QCDOrder = -1
        self.EWKOrder = -1
        self.ZPoleFocus = 0
        # -- 0 = turn on all EW correction / 1 = FSR off 
        # -- 2 = ISR off                   / 4 = ISRxFSR (interference) off
        # -- 7 = ISR, FSR, ISRxFSR off     / 8 = Weak off, but QED on
        self.EWControl = 0
        self.turnOffPhoton = 0

        self.minM = -1
        self.maxM = -1
        self.minZPt = 0
        self.maxZPt = 100000
        self.minZRap = -2000
        self.maxZRap = 2000
        self.minPtSub = 0.0
        self.maxPtSub = 100000.0
        self.minPtLead = 0.0
        self.maxPtLead = 100000.0
        self.minEtaSub = 0.0
        self.maxEtaSub = 100.0
        self.minEtaLead = 0.0
        self.maxEtaLead = 100.0

        # -- photon recombination
        self.dRDressed = 0.1

        self.PDF = ""

        # -- internal variables
        self.TIME = time.strftime('%Y%m%d', time.localtime(time.time()))



    def Generate(self):
        self.CheckMandatoryOptions()
        self.PrintOptions()

        self.GenerateParameterInput()
        self.GenerateHistogramInput()
        self.GenerateScript()


    def GenerateParameterInput(self):
        # -- TO DO: add self.scaleVarBy2 part
        fileName_param = self.MakeFileName( 'param' )

        str_muF = "{muF_:0.2f}d0".format(muF_=self.muF)
        str_muR = "{muR_:0.2f}d0".format(muR_=self.muR)

        if self.scaleVarBy2:
            str_muF = str_muF + " 2d0"
            str_muR = str_muR + " 2d0"

        f = open(fileName_param, "w")
        f.write(
"""=============================================
'CMS collision energy (GeV)    = ' {Energy_:0.0f}d0
=============================================
'Factorization scale  (GeV)    = ' {str_muF_}
'Renormalization scale  (GeV)  = ' {str_muR_}
=============================================
'Z production (pp=1,ppbar=2)   = ' 1
=============================================
Set to Alpha QED for incoming photon to 0 to turn off photon-induced (photon PDF dependent) channels
'Alpha QED for incoming photon = ' {alpha0Photon_}d0
'Alpha QED effective           = ' {alphaEff_}d0
'Fermi constant (1/Gev^2)      = ' 1.16637d-5
=============================================
'Lepton mass (GeV)             = ' {leptonMass_}d0
'W mass (GeV)                  = ' 80.403d0
'W width (GeV)                 = ' 2.141d0
'Z mass (GeV)                  = ' 91.1876d0
'Z width (GeV)                 = ' 2.4952d0
'Top mass (GeV)                = ' 172.9d0
'Higgs mass (GeV)              = ' 125d0
=============================================
Only QED corrections is on if the input scheme is manual
Input scheme: 0. Manual input; 1. Gmu scheme; 2. AlphaMz scheme; 3. alpha0 scheme
'Which input scheme:           = ' {inputScheme_:0.0f}
'sin^2(theta_w)                = ' 0.22255d0
'up quark charge               = ' 0.6666667d0
'down quark charge             = ' -0.3333333d0
'lepton charge                 = ' -1d0
'up quark vector coupling      = ' 0.4091d0
'down quark vector coupling    = ' -0.7045d0
'lepton vector coupling        = ' -0.11360d0
'up quark axial coupling       = ' -1d0
'down quark axial coupling     = ' 1d0
'lepton axial coupling         = ' 1d0
=============================================
Vegas Parameters
'Relative accuracy (in %)           = ' {relUnc_}d0
'Absolute accuracy                  = ' {absUnc_}d0
'Number of calls per iteration      = ' {nCall_:0.0f}
'Number of increase calls per iter. = ' {nIncreasedCall_:0.0f}
'Maximum number of evaluations      = ' {maxNEval_:0.0f}
'Random number seed for Vegas       = ' {randomSeed_:0.0f}
=============================================
'QCD Perturb. Order (0=LO, 1=NLO, 2=NNLO) = ' {QCDOrder_:0.0f}
'EW Perturb. Order (0=LO, 1=NLO)    = ' {EWKOrder_:0.0f}
'Z pole focus (1=Yes, 0=No) = ' {ZPoleFocus_:0.0f}
'EW control (leave 0 to keep all on) = ' {EWControl_:0.0f} 
'Turn off photon (1=Yes, 0=No, disabled if weak corr. is on) = ' {turnOffPhoton_:0.0f}
=============================================
'Lepton-pair invariant mass minimum = ' {minM_:0.1f}d0
'Lepton-pair invariant mass maximum = ' {maxM_:0.1f}d0
'Transverse mass minimum           = ' 0d0
'Transverse mass maximum           = ' 100000d0
'Z pT minimum                       = ' {minZPt_:0.2f}d0
'Z pT maximum                       = ' {maxZPt_:0.2f}d0
'Z rapidity minimum                 = ' {minZRap_}d0
'Z rapidity maximum                 = ' {maxZRap_}d0
'Lepton pT minimum                  = ' 0d0
'Lepton pT maximum                  = ' 100000d0
'Anti-lepton pT minimum             = ' 0.0d0
'Anti-lepton pT maximum             = ' 100000d0
'pT min for softer lepton           = ' {minPtSub_:0.1f}d0
'pT max for softer lepton           = ' {maxPtSub_:0.1f}d0
'pT min for harder lepton           = ' {minPtLead_:0.1f}d0
'pT max for harder lepton           = ' {maxPtLead_:0.1f}d0
Taking absolute value of lepton pseudorapidity?
'(yes = 1, no = 0)          = ' 1
'Lepton pseudorapidity minimum      = ' 0d0
'Lepton pseudorapidity maximum      = ' 100.0d0
Taking absolute value of anti-lepton pseudorapidity?
'(yes = 1, no = 0)          = ' 1
'Anti-lepton pseudorapidity minimum = ' 0d0
'Anti-lepton pseudorapidity maximum = ' 100.0d0
Taking absolute value of soft lepton pseudorapidity?
'(yes = 1, no = 0)                  = ' 1
'Softer lepton pseudorapidity min   = ' {minEtaSub_:0.2f}d0 
'Softer Lepton pseudorapidity max   = ' {maxEtaSub_:0.2f}d0
Taking absolute value of hard lepton pseudorapidity?
'(yes = 1, no = 0)                  = ' 1
'Harder lepton pseudorapidity min   = ' {minEtaLead_:0.2f}d0
'Harder Lepton pseudorapidity max   = ' {maxEtaLead_:0.2f}d0
PHOTON RECOMBINATION-----------------------------
'DeltaR sep. for photon recomb.     = ' {dRDressed_:0.2f}d0
'Minimum pT for observable photon   = ' 0.0d0
'Maximum eta for observable photon  = ' 100000d0
PHOTON CUTS--------------------------------------
'Minimum Number of Photon           = ' 0
'Maximum Number of Photon           = ' 1
JET DEFINITION-------------------------------
Jet Algorithm & Cone Size ('ktal'=kT algorithm, 'aktal'=anti-kT algorithm, 'cone'=cone)
'ktal, aktal or cone            = ' ktal
'Jet algorithm cone size (deltaR)   = ' 0.4d0
'DeltaR separation for cone algo    = ' 1.3
'Minimum pT for observable jets     = ' 0.0d0
'Maximum eta for observable jets    = ' 100000d0
JET CUTS--------------------------------------
'Minimum Number of Jets         = ' 0
'Maximum Number of Jets         = ' 2
'Min. leading jet pT                = ' 0d0
ISOLATION CUTS-------------------------------
'Lep-Anti-lep deltaR minimum        = ' 0.0d0
'Lep-Anti-lep deltaPhi min      = ' 0.0d0
'Lep-Anti-lep deltaPhi max      = ' 4.0d0
'Lep-Jet deltaR minimum             = ' 0.0d0
'Lep-Photon deltaR minimum          = ' 0.0d0
=============================================
Cut on Z rapidity for well-defined Collins-Soper Angles at pp Collider
'Z rapidity cutoff for CS frame     = ' 0.0d0
=============================================
(See manual for complete listing)
'PDF set =                        ' '{PDF_}'
'Turn off PDF error (1=Yes, 0=No)    = ' 0
(Active for MSTW2008 only, if PDF error is on:)
(Compute PDF+as errors: 1; just PDF errors: 0)
'Which alphaS                       = ' 0
(Active for MSTW2008 only; 0: 90 CL for PDFs+alphas, 1: 68 CL)
'PDF+alphas confidence level        = ' 1
=============================================""".format(
        Energy_=self.Energy,
        str_muF_=str_muF, str_muR_=str_muR,
        alpha0Photon_=self.alpha0Photon, alphaEff_=self.alphaEff,
        leptonMass_=self.leptonMass,
        inputScheme_=self.inputScheme,
        relUnc_=self.relUnc, absUnc_=self.absUnc,
        nCall_=self.nCall, nIncreasedCall_=self.nIncreasedCall, maxNEval_=self.maxNEval, randomSeed_=self.randomSeed,
        QCDOrder_=self.QCDOrder, EWKOrder_=self.EWKOrder, ZPoleFocus_=self.ZPoleFocus,
        EWControl_=self.EWControl, turnOffPhoton_=self.turnOffPhoton,
        minM_=self.minM, maxM_=self.maxM,
        minZPt_=self.minZPt, maxZPt_=self.maxZPt,
        minZRap_=self.minZRap, maxZRap_=self.maxZRap,
        minPtSub_=self.minPtSub, maxPtSub_=self.maxPtSub,
        minPtLead_=self.minPtLead, maxPtLead_=self.maxPtLead,
        minEtaSub_=self.minEtaSub, maxEtaSub_=self.maxEtaSub,
        minEtaLead_=self.minEtaLead, maxEtaLead_=self.maxEtaLead,
        dRDressed_=self.dRDressed,
        PDF_=self.PDF ))
        
        f.close()

        print "%s is generated" % fileName_param

    def GenerateHistogramInput(self):
        fileName_hist = self.MakeFileName( "hist" )

        minZPtEdge = self.minZPt
        maxZPtEdge = self.maxZPt
        if self.minZPt == 0 and self.maxZPt == 100000: # -- if it is full phase space
            minZPtEdge = 0
            maxZPtEdge = 100

        minZRapEdge = self.minZRap;
        maxZRapEdge = self.maxZRap;
        if self.minZRap == -2000 and self.maxZRap == 2000:
            minZRapEdge = -9.6
            maxZRapEdge = 9.6


        f = open(fileName_hist, "w")
        f.write(
"""HISTOGRAMS------(Order of Histograms Can Not Be Changed)----------------------
Name (DO NOT CHANGE)    Num Bins (<30)  Lower Bound Upper Bound Write Out (1=hist, 2=cuml, 3=both1&2, 4=rev-cuml, 5=both1&4, 0=none)
'1.  Z/W pT           ' 20      {minZPtEdge_:0.1f}d0     {maxZPtEdge_:0.1f}d0       1
'2.  Z/W eta          ' 24      {minZRapEdge_:0.1f}d0      {maxZRapEdge_:0.1f}d0       1
'3.  Q_ll inv mass    ' 20      {minM_:0.1f}d0        {maxM_:0.1f}d0       1
'4.  l-/lep. pT       ' 25      0d0     100d0       1
'5.  l-/lep. eta      ' 24      -9.6d0      9.6d0       1
'6.  l+/neut. pT      ' 25      0d0     100d0       1
'7.  l+/neut. eta     ' 24      -9.6d0      9.6d0       1
'8.  jet 1 pT         ' 20      0d0     100d0       1
'9.  jet 1 eta        ' 20      -5d0        5d0     1
'10. jet 2 pT         ' 20      0d0     100d0       1
'11. jet 2 eta        ' 20      -5d0        5d0     1
'12. photon pT        ' 20              0d0             100d0           1
'13. photon eta       ' 20              -5d0            5d0             1
'14. beam thrust      ' 20              0d0             100d0           1
'15. dR_l-l+          ' 20      0d0     5d0     0
'16. dR_j1,l-         ' 20      0d0     5d0     0
'17. dR_j1,l+         ' 20      0d0     5d0     0
'18. dR_j2,l-         ' 20      0d0     5d0     0
'19. dR_j2,l+         ' 20      0d0     5d0     0
'20. dR_j1j2          ' 20      0d0     5d0     0
'21. dR_phot,l+-      ' 20              0d0             5d0             0
'22. H_T          ' 20      0d0     200d0       0
'23. Mass_T           ' 20      0d0     1000d0      0
'24. A_FB vs Q_ll     ' 10              {minM_:0.1f}d0            {maxM_:0.1f}d0           0
====================================================================================
Moments (A_0, A_1, A_2) related to Collins-Soper Angles
'25. A_i vs Z pT      ' 10      0d0     100d0       1
'26. phi (CS Frame)   ' 10      -3.14159265d0   3.14159265d0    1
'27. cos(theta) (CS)  ' 10      -1d0        1d0     1
'28. dPhi_l-l+        ' 10      0d0     3.1415927d0 1
====================================================================================
Smoothing parameters
'Level (0 = none)     '  2
'Bin fraction (< 0.5) ' 1d-1
Method of combining iterations (0 = more reliable err. estimation; 1 = more consistent with tot. x-section)
'Method choice = ' 0
Histogram bin display (0 = bin central value, -1 = bin low edge, 1 = bin upper edge)
'Display option =' 0
""".format(
        minZPtEdge_=minZPtEdge, maxZPtEdge_=maxZPtEdge,
        minZRapEdge_=minZRapEdge, maxZRapEdge_=maxZRapEdge,
        minM_=self.minM, maxM_=self.maxM ) )

        f.close()
        print "%s is generated" % fileName_hist


    def GenerateScript(self):
        fileName_param = self.MakeFileName( 'param' )
        fileName_hist = self.MakeFileName( 'hist' )
        fileName_output = self.MakeFileName( 'output' )
        dirName = self.MakeFileName( 'dir' )

        orderName = "LO"
        if self.QCDOrder == 1: orderName = "NLO"
        elif self.QCDOrder == 2: orderName = "NNLO"

        fileName_script = self.MakeFileName( 'script' )
        f = open(fileName_script, "w")
        f.write(
"""#!/bin/bash

export SCRAM_ARCH=slc6_amd64_gcc630
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

# -- CMSSW enviornment -- #
cd /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_10_1_9 # -- has NNPDF3.1+luxQED PDF set
eval `scramv1 runtime -sh` # -- cmsenv

cd {FEWZBinPath_}

echo "run: ./local_run.sh z {dirName_} {fileName_param_} {fileName_hist_} {fileName_output_} ../ {nCore_}"
./local_run.sh z {dirName_} {fileName_param_} {fileName_hist_} {fileName_output_} ../ {nCore_}

echo "run: ./finish.sh {dirName_} {orderName_}.{fileName_output_}"
./finish.sh {dirName_} {orderName_}.{fileName_output_}

echo "job is completed"

""".format(
        dirName_=dirName, fileName_param_=fileName_param,
        fileName_hist_=fileName_hist, fileName_output_=fileName_output,
        nCore_=self.nCore, orderName_=orderName,
        FEWZBinPath_=self.FEWZBinPath) )

        f.close()
        print "%s is generated" % fileName_script


    def CheckMandatoryOptions(self):
        if self.tag == "":
            print "Set the tag"
            sys.exit()

        if self.FEWZBinPath == "":
            print "Set the path to FEWZ/bin"
            sys.exit()

        if self.nCore == 0:
            print "Set # cores"
            sys.exit()

        if self.muF == 9999 or self.muR == 9999:
            print "Set the scale"
            sys.exit()

        if self.relUnc == 0.0 and self.absUnc == 0.0: # -- check using "and": setting one of them is fine
            print "Set the uncertainty (relative or absolute)"
            sys.exit()

        if self.QCDOrder == -1 or self.EWKOrder == -1:
            print "Set QCD/EWK order"
            sys.exit()

        if self.minM == -1 or self.maxM == -1:
            print "Set minimum/maximum mass"
            sys.exit()

        if self.PDF == "":
            print "Set PDF"
            sys.exit()




    def PrintOptions(self):
        print "[CM energy]: %.1lf" % self.Energy

        print "[Scale]"
        print "   Factorization scale:   %lf" % self.muF
        print "   Renormalization scale: %lf" % self.muR
        if self.muF == 0 or self.muR == 0:
            print "   -> Running scale will be used"
        print "   Add additional jobs for scale variation by factor 2 (mu*1/2, mu*2)?: %d" % self.scaleVarBy2
        print ""

        print "[Coupling constant]"
        isPI = ""
        if self.alpha0Photon == 0:
            isPI = "NO PI contribution"
        else:
            isPI = "PI contribution is included"
        print "   alpha0 (for incoming photon): %lf -> %s" % (self.alpha0Photon, isPI)
        print "   alpha (effective):            %lf" % self.alphaEff
        print ""

        print "[Lepton type]"
        leptonType = ""
        if self.leptonMass == 0.10565837:
            leptonType = "MUON"
        elif self.leptonMass == 0.00051099895:
            leptonType = "ELECTRON"
        else:
            leptonType = "UNKNOWN"
        print "   lepton mass: %lf -> %s" % (self.leptonMass, leptonType)
        print ""

        print "[Scheme]"
        schemeType = ""
        if self.inputScheme == 1:
            schemeType = "Gmu scheme"
        elif self.inputScheme == 2:
            schemeType = "AlphaMz scheme"
        elif self.inputScheme == 3:
            schemeType = "Alpha0 scheme"
        elif  self.inputScheme == 0:
            schemeType = "Manual input"
        else:
            print "input scheme: %d -> unknown" % self.inputScheme
            sys.exit()            
        print "   Input scheme: %d (%s)" % (self.inputScheme, schemeType)
        print ""

        print "[Required precision]"
        print "   Relative uncertainty: %lf" % self.relUnc
        print "   Absolute uncertainty: %lf" % self.absUnc
        print "   Random seed: %d" % self.randomSeed
        print "   # calls per each iteration:             %d" % self.nCall
        print "   # increase of calls per each iteration: %d" % self.nIncreasedCall
        print "   # maximum evalution:                    %d" % self.maxNEval
        print ""

        QCDOrderType = ""
        if self.QCDOrder == 0: QCDOrderType = "LO"
        if self.QCDOrder == 1: QCDOrderType = "NLO"
        if self.QCDOrder == 2: QCDOrderType = "NNLO"
        EWKOrderType = ""
        if self.EWKOrder == 0: EWKOrderType = "LO"
        if self.EWKOrder == 1: EWKOrderType = "NLO"
        EWCorrType = ""
        if self.EWControl == 0:   EWCorrType = "All EW corrections are turned on"
        elif self.EWControl == 1: EWCorrType = "EW FSR Off"
        elif self.EWControl == 2: EWCorrType = "EW ISR Off"
        elif self.EWControl == 4: EWCorrType = "EW ISRxFSR (interference) off"
        elif self.EWControl == 7: EWCorrType = "EW ISR, FSR, ISRxFSR off"
        elif self.EWControl == 8: EWCorrType = "Weak off, but QED on"
        else:
            print "Unknown EWControl setting: %d" % self.EWControl
            sys.exit()

        print "[QCD/EWK setting]"
        print "   QCD order: %d (%s)" % (self.QCDOrder, QCDOrderType)
        print "   EWK order: %d (%s)" % (self.EWKOrder, EWKOrderType)
        print "   EWControl: %d (%s)" % (self.EWKOrder, EWCorrType)
        print "   Turn off photon?: %d" % self.turnOffPhoton
        print ""

        print "[Phase space]"
        print "   Dilepton mass range:     %.1lf < M(ll) < %.1lf" % (self.minM, self.maxM)
        print "   Dilepton pT range:       %.1lf < pT(ll) < %.1lf" % (self.minZPt, self.maxZPt)
        print "   Dilepton rapidity range: %.2lf < Y(ll) < %.2lf" % (self.minZRap, self.maxZRap)
        print ""
        print "   pT range of leading lepton:     %.1lf < pT < %.1lf" % (self.minPtLead, self.maxPtLead)
        print "   pT range of sub-leading lepton: %.1lf < pT < %.1lf" % (self.minPtSub, self.maxPtSub)
        print "   eta range of leading lepton:     %.2lf < |eta| < %.2lf" % (self.minEtaLead, self.maxEtaLead)
        print "   eta range of sub-leading lepton: %.2lf < |eta| < %.2lf" % (self.minEtaSub, self.maxEtaSub)
        print ""

        print "[Dressed lepton]"
        print "   DeltaR cone size: %.2lf" % self.dRDressed
        print ""

        print "[PDF]: %s" % self.PDF
        print ""

    # -- to have common format for the file name -- #
    def MakeFileName( self, fileType ):
        List_fileType = ["param", "hist", "script", "dir", "output"]
        if fileType not in List_fileType:
            print "fileType = %s is not the correct one. check the details"
            sys.exit()

        fileName = ""
        fileName_base = "v%s_%s" % (self.TIME, self.tag)

        if fileType == "dir":      fileName = fileName_base
        elif fileType == "output": fileName = "%s.dat" % fileName_base
        elif fileType == "script": fileName = "%s.sh" % fileName_base
        elif fileType == "param" or fileType == "hist":
            fileName = "%s_%s.txt" % (fileName_base, fileType )

        return fileName
