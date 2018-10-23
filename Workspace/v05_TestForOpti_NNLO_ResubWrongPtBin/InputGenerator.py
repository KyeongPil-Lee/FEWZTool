from Python.FEWZInputGenerator import FEWZInputGenerator
from Python.MultiScriptGenerator import MultiScriptGenerator

doNLOTest = True

list_massBinEdgePair = [
[15, 60], # -- below Z-peak
[60, 120], # -- Z-peak
[120, 1000], # -- above Z-peak
# [1000, 3000], # -- high-mass # -- not affected
]

list_diRapBinEdgePair = [ 
[0, 0.3],
[0.9, 1.2],
[1.8, 2.1],
]

list_scriptName = []
for massBinEdgePair in list_massBinEdgePair:
    minM = massBinEdgePair[0]
    maxM = massBinEdgePair[1]
    print "[%.0lf < M < %.0lf case]" % (minM, maxM)

    scale = (minM + maxM) / 2.0
    if minM == 60 and maxM == 120:
        scale = 91.18

    # -- calculation in each rapidity bin
    # for i in range( 0, len(list_diRapBinEdge)-1 ):
    for diRapBinEdgePair in list_diRapBinEdgePair:
        minY = diRapBinEdgePair[0]
        maxY = diRapBinEdgePair[1]

        generator = FEWZInputGenerator()
        # -- mandatory options
        generator.tag = "TestForBinOpti_Resub_M%.0lfto%.0lf_diRap%.1lfto%.1lf" % (minM, maxM, minY, maxY)
        generator.tag = generator.tag.replace(".", "p") # -- remove . in the file name: it makes error!!!

        generator.nCore = 24

        generator.FEWZPath = "/home/kplee/Physics/FEWZ/v03_absRapCut/FEWZ_3.1.rc" # -- absolute path!
        generator.WSPath = "/data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v05_TestForOpti_NNLO_ResubWrongPtBin" # -- absolute path!

        generator.muR = scale
        generator.muF = scale

        generator.relUnc = 0.1 # -- or generator.absUnc = XXX (absolute uncertainty is preferred)

        generator.QCDOrder = 2 # -- QCD@NNLO
        generator.EWKOrder = 1 # -- EWK@NLO

        generator.minM = minM
        generator.maxM = maxM

        generator.minZRap = minY
        generator.maxZRap = maxY

        # -- optional: see more options in Python/FEWZInputGenerator
        generator.ZPoleFocus = 0
        if minM == 60 and maxM == 120:
            generator.ZPoleFocus = 1

        generator.scaleVarBy2 = 0 # -- 2 more calculations if it is turned on
        generator.EWControl = 1 # -- turn-off FSR (mass cut in DY smaple is applied before FSR)
        generator.dRDressed = 0.0 # -- no dressing

        generator.PDF = "NNPDF31_nnlo_as_0118_luxqed"

        # -- bin_dileptonPt_v3p1: used for high-mass
        generator.useCustomHist = True
        generator.customHistPath = "./HistTemplate/histTemplate_M%dto%d.txt" % (minM, maxM)
        generator.list_binTextFile = ["bin_dileptonPt_v3.txt", "bin_dileptonPt_v3p1.txt", "bin_dileptonRapidity_v2.txt"] # -- should be in WSPath

        # -- NLO as a test
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
scriptGenerator.tag = "TestForBinOpti_Resub"
scriptGenerator.WSPath = "/data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v05_TestForOpti_NNLO_ResubWrongPtBin" # -- absolute path!
scriptGenerator.list_scriptName = list_scriptName
scriptGenerator.nJobPerScript = 3

if doNLOTest:
    scriptGenerator.tag = scriptGenerator.tag + "_NLO"
    scriptGenerator.nJobPerScript = 1

scriptGenerator.Generate()





