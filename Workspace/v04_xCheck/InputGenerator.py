from Python.FEWZInputGenerator import FEWZInputGenerator
from Python.MultiScriptGenerator import MultiScriptGenerator

list_massBinEdgePair = [
[50, 13000],
]

list_scriptName = []
for massBinEdgePair in list_massBinEdgePair:
    lowerEdge = massBinEdgePair[0]
    upperEdge = massBinEdgePair[1]
    print "[%.0lf < M < %.0lf case]" % (lowerEdge, upperEdge)

    # scale = (lowerEdge + upperEdge) / 2.0
    # if lowerEdge == 50 and upperEdge == 10000:
    #     scale = 91.18
    scale = 91.1876

    generator = FEWZInputGenerator()
    # -- mandatory options
    generator.tag = "ForXCheck_M%.0lfto%.0lf" % (lowerEdge, upperEdge)
    generator.nCore = 24

    generator.FEWZPath = "/home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc" # -- absolute path!
    generator.WSPath = "/data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v04_xCheck" # -- absolute path!

    generator.muR = scale
    generator.muF = scale

    generator.relUnc = 0.1 # -- or generator.absUnc = XXX (absolute uncertainty is preferred)
    generator.QCDOrder = 2 # -- QCD@NNLO
    generator.EWKOrder = 1 # -- EWK@NLO

    generator.minM = lowerEdge
    generator.maxM = upperEdge

    # -- optional: see more options in Python/FEWZInputGenerator
    generator.ZPoleFocus = 0
    if lowerEdge == 50 and upperEdge == 100:
        generator.ZPoleFocus = 1

    generator.alpha0Photon = 0.007297352568 # -- PI: turn on
    generator.scaleVarBy2 = 0 # -- too large time consumption!
    generator.EWControl = 1 # -- turn-off FSR (mass cut in DY smaple is applied before FSR)
    generator.dRDressed = 0.0 # -- no dressing

    generator.PDF = "NNPDF31_nnlo_as_0118_luxqed"

    generator.Generate()

    scriptName = generator.MakeFileName( 'script' )
    list_scriptName.append( scriptName )

scriptGenerator = MultiScriptGenerator()
scriptGenerator.tag = "ForXCheck"
scriptGenerator.WSPath = "/data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v04_xCheck" # -- absolute path!
scriptGenerator.list_scriptName = list_scriptName
scriptGenerator.nJobPerScript = 1
scriptGenerator.Generate()





