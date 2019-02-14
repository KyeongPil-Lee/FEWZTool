from Python.FEWZtoROOTHist import FEWZtoROOTHist

# list_PDF = [ "CT14nnlo_as_0118", "NNPDF31_nnlo_as_0118_luxqed"]
list_PDF = [ "CT14nnlo" ]

for PDF in list_PDF:
    tool = FEWZtoROOTHist()
    # tool.FEWZOutput = "NNLO.v20190207_FiducialXSec_Zpeak_%s.dat" % PDF
    tool.FEWZOutput = "NNLO.v20190211_FiducialXSec_Zpeak_%s.dat" % PDF
    tool.dic_histName = {    
        "l+/neu. eta":  "h_eta_muPlus",
        "l-/lep. eta":  "h_eta_muMinus",
        "Z/W rapidity": "h_diRap",
    }
    tool.outputFileName = "ROOTFile_FiducialXSec_Zpeak_%s.root" % (PDF)
    tool.Convert()

# FEWZFileName = "NNLO.v20190207_FiducialXSec_Zpeak_CT14nnlo_as_0118.dat"
# tool.FEWZOutput = "%s/%s" % (self.pathToFEWZFile, FEWZFileName)

# kinematicInfo = "M%.0lfto%.0lf_diRap%.1lfto%.1lf" % (minM, maxM, minY, maxY)
# kinematicInfo = kinematicInfo.replace(".", "p") # -- remove . in the file name
# FEWZFileName = self.FindFileNameByKinematicInfo( kinematicInfo )
# tool.FEWZOutput = "%s/%s" % (self.pathToFEWZFile, FEWZFileName)

# tool.dic_histName = {
#     "Z/W pT": "h_diPt_M%.0lfto%.0lf_Y%.1lfto%.1lf" % (minM, maxM, minY, maxY),
# }

# tool.isCustomBin = True
# tool.dic_customBin = { "Z/W pT": self.list_diPtBinEdge }

# tool.outputFileName = "ROOTFile_FEWZ_M%.0lfto%.0lf_Y%.1lfto%.1lf.root" % (minM, maxM, minY, maxY)

# tool.Convert()

