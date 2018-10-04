from Python.FEWZtoROOTHist import FEWZtoROOTHist

list_massBinEdgePair = [
[15, 60], # -- below Z-peak
[60, 120], # -- Z-peak
[120, 1000], # -- above Z-peak
[1000, 3000], # -- high-mass
]

list_diRapBinEdge = [ 0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 3.0, 4.0, 5.0, 100 ]
list_diPtBinEdge = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 1000 ]


for massBinEdgePair in list_massBinEdgePair:
    minM = massBinEdgePair[0]
    maxM = massBinEdgePair[1]
    print "[%.0lf < M < %.0lf case]" % (minM, maxM)

    # -- in each rapidity bin
    for i in range( 0, len(list_diRapBinEdge)-1 ):
        minY = list_diRapBinEdge[i]
        maxY = list_diRapBinEdge[i+1]

        tool = FEWZtoROOTHist()
        tool.FEWZOutput = "NLO.v20181002_TestForBinOpti_M%.0lfto%.0lf_diRap%.1lfto%.1lf_NLO.dat" % (minM, maxM, minY, maxY)

        tool.dic_histName = {
            "Z/W pT": "h_diPt_M%.0lfto%.0lf_diRap%.1lfto%.1lf" % (minM, maxM, minY, maxY),
        }

        tool.isCustomBin = True
        tool.dic_bin = {
            "Z/W pT": list_diPtBinEdge
        }

        tool.outputFileName = "ROOTFile_FEWZ_TestForBinOpti_M%.0lfto%.0lf_diRap%.1lfto%.1lf.root" % (minM, maxM, minY, maxY)

        tool.Convert()