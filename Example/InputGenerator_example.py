from Python.FEWZInputGenerator import FEWZInputGenerator

generator = FEWZInputGenerator()
# -- mandatory options
generator.tag = "Example"
generator.nCore = 24
generator.FEWZPath = "/home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc/" # -- absolute path!
generator.WSPath = "/data9/Users/kplee/FEWZTool/master/Example" # -- absolute path!

generator.muR = 91.2
generator.muF = 91.2

generator.relUnc = 0.1 # -- or generator.absUnc = XXX (absolute uncertainty is preferred)
generator.QCDOrder = 1
generator.EWKOrder = 0

generator.minM = 60
generator.maxM = 120

# -- optional: see more options in Python/FEWZInputGenerator
generator.ZPoleFocus = 1
generator.scaleVarBy2 = 1

# -- optional: if you use custom histogram .txt file
# generator.useCustomHist = True
# generator.customHistPath = "./HistTemplate/histTemplate_M%dto%d.txt" % (minM, maxM)
# -- these text files will be copied to FEWZBath/bin before running FEWZ
# generator.list_binTextFile = ["bin_dileptonPt_v3.txt", "bin_dileptonPt_v3p1.txt", "bin_dileptonRapidity_v2.txt"] # -- should be in WSPath

generator.PDF = "NNPDF31_nnlo_as_0118"

generator.Generate()

# -- for generating script for running multiple FEWZ jobs:
# -- It can be done by Python/MultiScriptGenerator.py
# -- example: https://github.com/KyeongPil-Lee/FEWZTool/blob/v01_Reweighting/Workspace/v03_TestForBinOpti_NNLO/InputGenerator_TestForBinOpti.py
