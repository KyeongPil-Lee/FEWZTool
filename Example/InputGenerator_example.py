from Python.FEWZInputGenerator import FEWZInputGenerator

generator = FEWZInputGenerator()
# -- mandatory options
generator.tag = "Example"
generator.nCore = 24
generator.FEWZBinPath = "/home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc/bin" # -- absolute path!

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

generator.PDF = "NNPDF31_nnlo_as_0118"

generator.Generate()
