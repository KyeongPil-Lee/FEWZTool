from Python.FEWZtoROOTHist import FEWZtoROOTHist

list_massBinEdgePair = [
[15, 60], # -- below Z-peak
[60, 120], # -- Z-peak
[120, 1000], # -- above Z-peak
[1000, 3000], # -- high-mass
]

list_diRapBinEdge = [ 0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 100.0 ]
# list_diRapBinEdge = [ 0, 0.3 ] # -- test
# list_diPtBinEdge1 = [ 0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 1000 ] # -- for low mass range: but it was not used in FEWZ calc due to unknown reason :(
list_diPtBinEdge2 = [ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 1000 ] # -- highest mass range


for massBinEdgePair in list_massBinEdgePair:
    minM = massBinEdgePair[0]
    maxM = massBinEdgePair[1]
    print "[%.0lf < M < %.0lf case]" % (minM, maxM)

    # -- in each rapidity bin
    for i in range( 0, len(list_diRapBinEdge)-1 ):
        minY = list_diRapBinEdge[i]
        maxY = list_diRapBinEdge[i+1]

        tool = FEWZtoROOTHist()

        tag = "TestForBinOpti_M%.0lfto%.0lf_diRap%.1lfto%.1lf" % (minM, maxM, minY, maxY)
        tag = tag.replace(".", "p") # -- remove . in the file name: it makes error!!!
        tool.FEWZOutput = "NNLO.v20181007_%s.dat" % (tag)

        tool.dic_histName = {
            "Z/W pT": "h_diPt_M%.0lfto%.0lf_diRap%.1lfto%.1lf" % (minM, maxM, minY, maxY),
        }

        tool.isCustomBin = True
        tool.dic_customBin = { "Z/W pT": list_diPtBinEdge2 }
        # if minM == 1000 and maxM == 3000:
        #     tool.dic_customBin = { "Z/W pT": list_diPtBinEdge2 }
        # else:
        #     tool.dic_customBin = { "Z/W pT": list_diPtBinEdge1 }

        tool.outputFileName = "ROOTFile_FEWZ_TestForBinOpti_M%.0lfto%.0lf_diRap%.1lfto%.1lf.root" % (minM, maxM, minY, maxY)

        tool.Convert()

mergedFileName = "ROOTFile_FEWZ_TestForBinOpti_NNLO.root"
print "+++ hadd command +++"
print "hadd %s *.root" % mergedFileName