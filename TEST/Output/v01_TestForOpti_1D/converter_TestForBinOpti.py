from Python.FEWZtoROOTHist import FEWZtoROOTHist

list_binEdge_diRap =
[ 
    0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4,
    3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 
    20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 1000.0
]

list_binEdge_diPt =
[  
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
    200, 300, 400, 500, 600, 700, 800, 900, 1000
]

tool = FEWZtoROOTHist()

tool.FEWZOutput = "NNLO.v20180925_TestForBinOpti_M15to60.dat"
tool.dic_histName = {
    "Z/W pT":   "h_diPt",
    "Z/W rapidity": "h_diRap",
}

tool.isCustomBin = True
tool.dic_bin = {
    "Z/W pT": list_binEdge_diPt
    "Z/W rapidity": list_binEdge_diRap
}

tool.outputFileName = "ROOTFile_FEWZ_TestForBinOpti_M15to60.root"

tool.Convert()