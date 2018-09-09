import sys, math
from ROOT import TFile, TH1D

class FEWZtoROOTHist:
    def __init__(self):
        self.FEWZOutput = ""
        self.dic_histName = []
        self.outputFileName = ""

    def Convert(self):
        print "+" * 100
        print "Warning: currently only the histograms with equal bin width are supported"
        print "+" * 100
        self.CheckOptions()
        self.PrintOptions()

        f_output = TFile(self.outputFileName, "RECREATE")
        f_output.cd()

        for FEWZHistName in self.dic_histName.keys():
            (h_temp, h_temp_integErr, h_temp_PDFErr) = self.ConvertToTH1D(FEWZHistName)
            h_temp.Write()
            h_temp_integErr.Write()
            h_temp_PDFErr.Write()

        f_output.Close()

    def ConvertToTH1D(self, FEWZHistName):
        print "[ConvertToTH1D] FEWZ histogram name: %s" % FEWZHistName
        f = open(self.FEWZOutput, "r")

        # -- find the bin values in FEWZ output
        list_binValue = []

        isFound = False
        lines = f.readlines()
        for line in lines:
            # -- numbers in each bin
            list_number = []
            if isFound:
                if "----" in line: # -- if the histogram is finished -- #
                    break
                else:
                    for item in line.split():
                        if self.isNumber(item):
                            list_number += [float(item)]

                if len(list_number) == 4:
                    print "\t(BinCenter, X-sec, Integration error, PDF error (symmetric)) = (%lf, %lf, %lf, %lf)" % (list_number[0], list_number[1], list_number[2], list_number[3])
                    dic_binValue = {
                    "binCenter":  list_number[0],
                    "binContent": list_number[1],
                    "integErr":   list_number[2],
                    "PDFErr":     list_number[3],
                    }
                    list_binValue.append( dic_binValue )

            if FEWZHistName in line:
                isFound = True


        nBin = len(list_binValue)
        if nBin == 0:
            print "No corresponding histogram is found (FEWZ hist name: %s)" % (FEWZHistName)
            sys.exit()

        binWidth = list_binValue[1]["binCenter"] - list_binValue[0]["binCenter"]
        lowerEdge = list_binValue[0]["binCenter"] - (binWidth / 2.0)
        upperEdge = list_binValue[-1]["binCenter"] + (binWidth / 2.0)

        # h_ROOT = TH1D(self.dic_histName[FEWZHistName], "", nBin, array("d", list_binEdge) )
        h_ROOT = TH1D(self.dic_histName[FEWZHistName], "", nBin, lowerEdge, upperEdge )
        h_ROOT_integErr = TH1D(self.dic_histName[FEWZHistName]+"_integErr", "", nBin, lowerEdge, upperEdge )
        h_ROOT_PDFErr = TH1D(self.dic_histName[FEWZHistName]+"_PDFErr", "", nBin, lowerEdge, upperEdge )

        for i in range(0, nBin):
            i_bin = i+1

            binValue = list_binValue[i]

            h_ROOT.SetBinContent(i_bin, binValue["binContent"])

            integErr = binValue["integErr"]
            PDFErr = binValue["PDFErr"]
            error = math.sqrt( integErr*integErr + PDFErr*PDFErr )

            h_ROOT.SetBinError(i_bin, error)

            h_ROOT_integErr.SetBinContent(i_bin, integErr)
            h_ROOT_integErr.SetBinError(i_bin, 0)

            h_ROOT_PDFErr.SetBinContent(i_bin, PDFErr)
            h_ROOT_PDFErr.SetBinError(i_bin, 0)

        print "   Successfully converted (ROOT histogram name: %s)" % self.dic_histName[FEWZHistName]
        return (h_ROOT, h_ROOT_integErr, h_ROOT_PDFErr)

    def CheckOptions(self):
        if self.FEWZOutput == "" or \
           len(self.dic_histName) == 0 or \
           self.outputFileName == "":
           print "Mandatory options are missing ... please check"
           self.PrintOptions()

    def PrintOptions(self):
        print "FEWZ output to be read: ", self.FEWZOutput
        print "list of histograms that will be converted to ROOT histogram (TH1D): "
        for FEWZHistName in self.dic_histName.keys():
            print "   %s (FEWZ) -> %s (ROOT)" % (FEWZHistName, self.dic_histName[FEWZHistName])
        print "output file name:", self.outputFileName

    def isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False