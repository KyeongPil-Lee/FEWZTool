from Python.FEWZInputGenerator import FEWZInputGenerator

# doNLOTest = True
doNLOTest = False

list_PDF = [
# "NNPDF31_nnlo_as_0118_luxqed",
# "CT14nnlo_as_0118", # -- only have 0.118 result without error set
"CT14nnlo", # -- central value: alpha_s = 0.118 w/ all error sets
]

for PDF in list_PDF:
    generator = FEWZInputGenerator()

    # -- mandatory options
    generator.tag = "FiducialXSec_Zpeak_%s" % (PDF)

    # -- 8, 12, 24 ...
    generator.nCore = 24

    generator.FEWZPath = "/home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc" # -- absolute path!
    generator.WSPath = "/data9/Users/kplee/FEWZTool/v05_rapidityInFid/Workspace/v01_electron" # -- absolute path!

    generator.leptonMass = 0.00051099895 # -- electron

    generator.muR = 91.19
    generator.muF = 91.19

    generator.relUnc = 0.1 # -- or generator.absUnc = XXX (absolute uncertainty is preferred)

    generator.QCDOrder = 2 # -- QCD@NNLO
    generator.EWKOrder = 1 # -- EWK@NLO

    generator.minM = 60
    generator.maxM = 120

    generator.minPtSub = 17.0
    generator.maxPtSub = 100000.0
    generator.minPtLead = 28.0
    generator.maxPtLead = 100000.0
    generator.minEtaSub = 0.0
    generator.maxEtaSub = 2.4
    generator.minEtaLead = 0.0
    generator.maxEtaLead = 2.4

    generator.ZPoleFocus = 1

    generator.scaleVarBy2 = 0 # -- 2 more calculations if it is turned on
    generator.EWControl = 0 # -- Turn on all ISR/FSR effect
    generator.dRDressed = 0.0 # -- no dressing

    generator.PDF = PDF

    generator.useCustomHist = True
    generator.customHistPath = "./HistTemplate/histTemplate.txt"

    # -- NLO as a test
    if doNLOTest:
        # -- use NLO PDFs
        if "NNPDF" in generator.PDF:
            generator.PDF = "NNPDF31_nlo_as_0118"
        if "CT14" in generator.PDF:
            generator.PDF = "CT14nlo_as_0118"

        generator.tag = "FiducialXSec_Zpeak_%s" % (generator.PDF)
        generator.tag = generator.tag + "_NLO"
        generator.nCore = 1
        generator.QCDOrder = 1 # -- QCD@NLO
        generator.EWKOrder = 0 # -- EWK@LO

    generator.Generate()

