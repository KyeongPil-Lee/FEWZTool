from Python.FEWZInputGenerator import FEWZInputGenerator
from Python.MultiScriptGenerator import MultiScriptGenerator

list_massBinEdgePair = [
[14.5, 50],
]

list_scriptName = []
for massBinEdgePair in list_massBinEdgePair:
    minM = massBinEdgePair[0]
    maxM = massBinEdgePair[1]
    print "[%.0lf < M < %.0lf case]" % (minM, maxM)

    scale = (minM + maxM) / 2.0

    generator = FEWZInputGenerator()

    # -- mandatory options
    generator.tag = "LowMassTest_M%.1lfto%.1lf" % (minM, maxM)
    generator.tag = generator.tag.replace(".", "p") # -- remove . in the file name: it makes error!!!

    generator.nCore = 24

    # -- tamsa2
    generator.FEWZPath = "/home/kplee/Physics/FEWZ/v03_absRapCut/FEWZ_3.1.rc" # -- absolute path!
    generator.WSPath = "/data9/Users/kplee/FEWZTool/v02_LowMass/Workspace/v04_M14p5to50_AbsErr" # -- absolute path!

    generator.muR = scale
    generator.muF = scale

    # generator.relUnc = 0.1 # -- or generator.absUnc = XXX (absolute uncertainty is preferred)
    generator.absUnc = 2756.99 * 0.001 # -- 0.1% w.r.t. central value

    generator.QCDOrder = 2 # -- QCD@NNLO
    generator.EWKOrder = 1 # -- EWK@NLO

    generator.minM = minM
    generator.maxM = maxM

    # -- optional: see more options in Python/FEWZInputGenerator
    generator.ZPoleFocus = 0
    # if minM == 60 and maxM == 120:
    #     generator.ZPoleFocus = 1

    generator.scaleVarBy2 = 0 # -- 2 more calculations if it is turned on
    generator.EWControl = 1 # -- turn-off FSR (mass cut in DY smaple is applied before FSR)
    generator.dRDressed = 0.0 # -- no dressing

    generator.PDF = "NNPDF31_nnlo_as_0118_luxqed"

    generator.Generate()

    scriptName = generator.MakeFileName( 'script' )
    list_scriptName.append( scriptName )


scriptGenerator = MultiScriptGenerator()
scriptGenerator.tag = "LowMassTest"
scriptGenerator.WSPath = "/data9/Users/kplee/FEWZTool/v02_LowMass/Workspace/v04_M14p5to50_AbsErr" # -- tamsa2
scriptGenerator.list_scriptName = list_scriptName
# scriptGenerator.nJobPerScript = 2
scriptGenerator.nJobPerScript = 1
scriptGenerator.Generate()





