from Python.FEWZInputGenerator import FEWZInputGenerator
from Python.MultiScriptGenerator import MultiScriptGenerator

# doNLOTest = True
doNLOTest = False

list_massBinEdgePair = [
[10, 50],
]

list_minZPt = [0.2, 0.4, 0.6, 0.8, 1.0]

list_scriptName = []
for massBinEdgePair in list_massBinEdgePair:
    minM = massBinEdgePair[0]
    maxM = massBinEdgePair[1]
    print "[%.0lf < M < %.0lf case]" % (minM, maxM)

    scale = (minM + maxM) / 2.0

    for minZPt in list_minZPt:
        generator = FEWZInputGenerator()

        # -- mandatory options
        generator.tag = "LowMassTestZPtScan_LargerNcall_M%.1lfto%.1lf_minZPt%.1lf" % (minM, maxM, minZPt)
        generator.tag = generator.tag.replace(".", "p") # -- remove . in the file name: it makes error!!!

        generator.nCore = 8
        generator.nCall = 20000000

        # -- tamsa2
        generator.FEWZPath = "/home/kplee/Physics/FEWZ/v03_absRapCut/FEWZ_3.1.rc" # -- absolute path!
        generator.WSPath = "/data9/Users/kplee/FEWZTool/v02_LowMass/Workspace/v06_ZPtScan_LargerNCall" # -- absolute path!

        generator.muR = scale
        generator.muF = scale

        generator.relUnc = 0.1 # -- or generator.absUnc = XXX (absolute uncertainty is preferred)

        generator.QCDOrder = 2 # -- QCD@NNLO
        generator.EWKOrder = 1 # -- EWK@NLO

        generator.minM = minM
        generator.maxM = maxM

        generator.minZPt = minZPt
        generator.maxZPt = 100000.0

        # -- optional: see more options in Python/FEWZInputGenerator
        generator.ZPoleFocus = 0
        # if minM == 60 and maxM == 120:
        #     generator.ZPoleFocus = 1

        generator.scaleVarBy2 = 0 # -- 2 more calculations if it is turned on
        generator.EWControl = 1 # -- turn-off FSR (mass cut in DY smaple is applied before FSR)
        generator.dRDressed = 0.0 # -- no dressing

        generator.PDF = "NNPDF31_nnlo_as_0118_luxqed"

        if doNLOTest:
            generator.tag = generator.tag + "_NLO"
            generator.nCore = 1
            generator.QCDOrder = 1 # -- QCD@NLO
            generator.EWKOrder = 0 # -- EWK@LO
            generator.PDF = "NNPDF31_nlo_as_0118_luxqed"

        generator.Generate()

        scriptName = generator.MakeFileName( 'script' )
        list_scriptName.append( scriptName )


scriptGenerator = MultiScriptGenerator()
scriptGenerator.tag = "LowMassTestZPtScan_LargerNcall"
scriptGenerator.WSPath = "/data9/Users/kplee/FEWZTool/v02_LowMass/Workspace/v06_ZPtScan_LargerNCall" # -- tamsa2
scriptGenerator.list_scriptName = list_scriptName
# scriptGenerator.nJobPerScript = 2
scriptGenerator.nJobPerScript = 1

if doNLOTest:
    scriptGenerator.tag = scriptGenerator.tag + "_NLO"
    scriptGenerator.nJobPerScript = 1
    
scriptGenerator.Generate()





