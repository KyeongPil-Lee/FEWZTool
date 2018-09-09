from Python.FEWZtoROOTHist import FEWZtoROOTHist

tool = FEWZtoROOTHist()
tool.FEWZOutput = "NNLO.v20180906_M60to120_NoDressed_withinAcc.dat"
tool.dic_histName = {
    "Q_ll Invaria": "h_mass",
    "l-/lep. pT":   "h_pt_minus",
    "l-/lep. eta":  "h_eta_minus",
    "l+/neu. pT":   "h_pt_plus",
    "l+/neu. eta":  "h_eta_plus",
}
tool.outputFileName = "ROOTFile_HistogramFromFEWZ.root"

tool.Convert()