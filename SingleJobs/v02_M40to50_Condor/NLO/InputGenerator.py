from Python.FEWZInputGenerator import FEWZInputGenerator
# from Python.MultiScriptGenerator import MultiScriptGenerator
from Python.CondorScriptGenerator import CondorScriptGenerator

import os

doNLOTest = True
# doNLOTest = False

list_massBinEdgePair = [
[40, 50],
]

for massBinEdgePair in list_massBinEdgePair:
    minM = massBinEdgePair[0]
    maxM = massBinEdgePair[1]
    print "[%.0lf < M < %.0lf case]" % (minM, maxM)

    scale = (minM + maxM) / 2.0
    ZMass = 91.18
    if minM < ZMass and ZMass < maxM:  # -- minM < ZMass < maxM
        scale = ZMass

    generator = FEWZInputGenerator()
    # -- mandatory options
    generator.tag = "XSecForDYSamplePerSector_M%.0lfto%.0lf" % (minM, maxM)

    # -- 8, 12, 24 ...
    generator.nCore = 1 # -- 1 core per sector

    generator.muR = scale
    generator.muF = scale

    generator.relUnc = 0.1 # -- or generator.absUnc = XXX (absolute uncertainty is preferred)

    generator.QCDOrder = 2 # -- QCD@NNLO
    generator.EWKOrder = 1 # -- EWK@NLO

    generator.minM = minM
    generator.maxM = maxM

    # -- optional: see more options in Python/FEWZInputGenerator
    generator.ZPoleFocus = 0
    if minM < ZMass and ZMass < maxM: # -- minM < ZMass < maxM
        generator.ZPoleFocus = 1

    generator.scaleVarBy2 = 0 # -- 2 more calculations if it is turned on
    generator.EWControl = 1 # -- turn-off FSR (mass cut in DY smaple is applied before FSR)
    generator.dRDressed = 0.0 # -- no dressing

    generator.PDF = "NNPDF31_nnlo_as_0118_luxqed"

    # -- NLO as a test
    if doNLOTest:
        generator.tag = generator.tag + "_NLO"
        generator.nCore = 1
        generator.QCDOrder = 1 # -- QCD@NLO
        generator.EWKOrder = 0 # -- EWK@LO
        generator.PDF = "NNPDF31_nlo_as_0118_luxqed"

    generator.Generate()

    ################################################
    # -- generate scripts for condor submission -- #
    ################################################
    condorGenerator = CondorScriptGenerator()

    condorGenerator.FEWZInputGenerator = generator
    condorGenerator.FEWZBinPath = "/data9/Users/kplee/FEWZPackage/LHAPDF_621/FEWZ_3.1.rc/bin" # -- absolute path!
    condorGenerator.WSPath = os.getcwd() # -- absolute path!

    condorGenerator.Generate()


    # scriptName = generator.MakeFileName( 'script' )
    # list_scriptName.append( scriptName )


# scriptGenerator = MultiScriptGenerator()
# scriptGenerator.tag = "XSecForDYSample"
# scriptGenerator.WSPath = os.getcwd() # -- absolute path!
# scriptGenerator.list_scriptName = list_scriptName
# scriptGenerator.nJobPerScript = 1

# if doNLOTest:
#     scriptGenerator.tag = scriptGenerator.tag + "_NLO"
#     scriptGenerator.nJobPerScript = 1

# scriptGenerator.Generate()

# scriptGenerator = CondorScriptGenerator()
# scriptGenerator.list_scriptName = list_scriptName
# scriptGenerator.nCore = nCPUCore
# scriptGenerator.Generate()

