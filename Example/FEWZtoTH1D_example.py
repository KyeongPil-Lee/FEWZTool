from Python.FEWZtoROOTHist import FEWZtoROOTHist

tool = FEWZtoROOTHist()
tool.FEWZOutput = "NLO.v20181010_Example.dat"

tool.dic_histName = {
    "Z/W pT": "h_diPt",
    "Z/W rapidity": "h_diRap",
}

# -- The code will assume uniform bin size
# -- if you need histogram with non-uniform bin size, you can use below option
# list_diPtBinEdge = [ 0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 1000 ]
# tool.isCustomBin = True
# tool.dic_customBin = {
#     "Z/W pT": list_diPtBinEdge
# }

tool.outputFileName = "ROOTFile_FEWZ_Example.root"

tool.Convert()