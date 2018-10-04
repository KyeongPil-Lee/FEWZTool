from Python.FEWZInputGenerator import FEWZInputGenerator
from Python.MultiScriptGenerator import MultiScriptGenerator

list_massBinEdgePair = [
[15, 60], # -- below Z-peak
[60, 120], # -- Z-peak
[120, 1000], # -- above Z-peak
[1000, 3000], # -- high-mass
]

# list_scriptName = []
for massBinEdgePair in list_massBinEdgePair:
    lowerEdge = massBinEdgePair[0]
    upperEdge = massBinEdgePair[1]
    print "[%.0lf < M < %.0lf case]" % (lowerEdge, upperEdge)

    scale = (lowerEdge + upperEdge) / 2.0
    if lowerEdge == 60 and upperEdge == 120:
        scale = 91.18

    generator = FEWZInputGenerator()
    # -- mandatory options
    generator.tag = "TestForBinOpti_M%.0lfto%.0lf" % (lowerEdge, upperEdge)
    generator.nCore = 24
    generator.FEWZBinPath = "/home/kplee/Physics/FEWZ/v02_absRap/FEWZ_3.1.rc/bin" # -- absolute path!

    generator.muR = scale
    generator.muF = scale

    generator.relUnc = 0.1 # -- or generator.absUnc = XXX (absolute uncertainty is preferred)
    generator.QCDOrder = 2 # -- QCD@NNLO
    generator.EWKOrder = 1 # -- EWK@NLO

    generator.minM = lowerEdge
    generator.maxM = upperEdge

    # -- optional: see more options in Python/FEWZInputGenerator
    generator.ZPoleFocus = 0
    if lowerEdge == 60 and upperEdge == 120:
        generator.ZPoleFocus = 1

    generator.scaleVarBy2 = 0 # -- 2 more calculations if it is turned on
    generator.EWControl = 1 # -- turn-off FSR (mass cut in DY smaple is applied before FSR)
    generator.dRDressed = 0.0 # -- no dressing

    generator.PDF = "NNPDF31_nnlo_as_0118"

    generator.useCustomHist = True
    generator.customHistPath = "./HistTemplate/histTemplate_M%dto%d.txt" % (lowerEdge, upperEdge)

    generator.Generate()

    scriptName = generator.MakeFileName( 'script' )
    # list_scriptName.append( scriptName )

# scriptGenerator = MultiScriptGenerator()
# scriptGenerator.tag = "XSecForDYSample"
# scriptGenerator.FEWZBinPath = "/home/kplee/Physics/FEWZ/v02_absRap/FEWZ_3.1.rc/bin" # -- absolute path!
# scriptGenerator.list_scriptName = list_scriptName
# scriptGenerator.nJobPerScript = 3
# scriptGenerator.Generate()





