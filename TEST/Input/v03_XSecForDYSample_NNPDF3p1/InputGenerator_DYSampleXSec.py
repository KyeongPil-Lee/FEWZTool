from Python.FEWZInputGenerator import FEWZInputGenerator
from Python.MultiScriptGenerator import MultiScriptGenerator

list_massBinEdgePair = [
[10, 50],
[15, 50], # -- because 10 < M < 15 GeV diverges
[50, 100],
[50, 200], # -- if 100 < M < 200 Sample is not used
[50, 10000], # -- for M > 50 GeV sample (ex> DY->tautau)
[100, 200],
[200, 400],
[400, 500],
[500, 700],
[700, 800],
[800, 1000],
[1000, 1500],
[1500, 2000],
[2000, 3000],
]

list_scriptName = []
for massBinEdgePair in list_massBinEdgePair:
    lowerEdge = massBinEdgePair[0]
    upperEdge = massBinEdgePair[1]
    print "[%.0lf < M < %.0lf case]" % (lowerEdge, upperEdge)

    scale = (lowerEdge + upperEdge) / 2.0
    if lowerEdge == 50 and upperEdge == 10000:
        scale = 91.18

    generator = FEWZInputGenerator()
    # -- mandatory options
    generator.tag = "XSecForDYSample_M%.0lfto%.0lf" % (lowerEdge, upperEdge)
    generator.nCore = 24
    generator.FEWZBinPath = "/home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc/bin" # -- absolute path!

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

    generator.scaleVarBy2 = 1
    generator.EWControl = 1 # -- turn-off FSR (mass cut in DY smaple is applied before FSR)
    generator.dRDressed = 0.0 # -- no dressing

    generator.PDF = "NNPDF31_nnlo_as_0118"

    generator.Generate()

    scriptName = generator.MakeFileName( 'script' )
    list_scriptName.append( scriptName )

scriptGenerator = MultiScriptGenerator()
scriptGenerator.tag = "XSecForDYSample"
scriptGenerator.FEWZBinPath = "/home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc/bin" # -- absolute path!
scriptGenerator.list_scriptName = list_scriptName
scriptGenerator.nJobPerScript = 3
scriptGenerator.Generate()





