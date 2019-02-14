import sys, math
from ROOT import TFile, TH1D
from array import array

class FEWZtoROOTHist:
    def __init__(self):
        self.FEWZOutput = ""
        self.dic_histName = []
        self.outputFileName = ""
        self.isCustomBin = False
        self.dic_customBin = {}

    def Convert(self):
        # print "+" * 100
        # print "Warning: currently only the histograms with equal bin width are supported"
        # print "+" * 100
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
        print "Done.\n"

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
                            # print "line = ", line
                            # print "  -> list_number: ", list_number

                if len(list_number) == 4:
                    print "\t(BinCenter, X-sec, Integration error, PDF error (symmetric)) = (%lf, %lf, %lf, %lf)" % (list_number[0], list_number[1], list_number[2], list_number[3])
                    dic_binValue = {
                    "binCenter":  list_number[0],
                    "binContent": list_number[1],
                    "integErr":   list_number[2],
                    "PDFErr":     list_number[3],
                    }
                    list_binValue.append( dic_binValue )

                if len(list_number) == 3:
                    print "\t(BinCenter, X-sec, Integration error, PDF error (no info.)) = (%lf, %lf, %lf, %lf)" % (list_number[0], list_number[1], list_number[2], 0)
                    dic_binValue = {
                    "binCenter":  list_number[0],
                    "binContent": list_number[1],
                    "integErr":   list_number[2],
                    "PDFErr":     0,
                    }
                    list_binValue.append( dic_binValue )

                if len(list_number) == 5:
                    print "\t(BinCenter, X-sec, Integration error, PDF error+, PDF error-) = (%lf, %lf, %lf, %lf, %lf)" % (list_number[0], list_number[1], list_number[2], list_number[3], list_number[4])
                    dic_binValue = {
                    "binCenter":  list_number[0],
                    "binContent": list_number[1],
                    "integErr":   list_number[2],
                    "PDFErr+":    list_number[3],
                    "PDFErr-":    list_number[4],
                    "PDFErr":     list_number[3] if list_number[3] > list_number[4] else list_number[4] # -- take the larger uncertainty
                    }
                    list_binValue.append( dic_binValue )

            if FEWZHistName in line:                
                isFound = True


        nBin = len(list_binValue)
        if nBin == 0:
            print "No corresponding histogram is found (FEWZ hist name: %s)" % (FEWZHistName)
            sys.exit()

        
        if self.isCustomBin and FEWZHistName in self.dic_customBin.keys():
            (h_ROOT, h_ROOT_integErr, h_ROOT_PDFErr) = self.ProduceTH1D_CustomBin(list_binValue, FEWZHistName )
            return (h_ROOT, h_ROOT_integErr, h_ROOT_PDFErr)

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

    def ProduceTH1D_CustomBin(self, list_binValue, FEWZHistName ):
        list_binEdge = self.dic_customBin[FEWZHistName]
        nBin = len(list_binEdge) - 1
        nPoint = len(list_binValue)
        # print "(nBin, nPoint) = (%d, %d)" % (nBin, nPoint)
        
        if nBin != nPoint:
            print "(nBin from customized bin, nPoint) = (%d, %d): NOT SAME!" % (nBin, nPoint)
            sys.exit()

        h_ROOT          = TH1D(self.dic_histName[FEWZHistName],             "", nBin, array("d", list_binEdge) )
        h_ROOT_integErr = TH1D(self.dic_histName[FEWZHistName]+"_integErr", "", nBin, array("d", list_binEdge) )
        h_ROOT_PDFErr   = TH1D(self.dic_histName[FEWZHistName]+"_PDFErr",   "", nBin, array("d", list_binEdge) )

        for i in range(0, nBin):
            i_bin = i+1

            binValue = list_binValue[i]

            binCenter = binValue["binCenter"]
            binCenter_fromCustomBin = ( list_binEdge[i] + list_binEdge[i+1] ) / 2.0
            if binCenter != binCenter_fromCustomBin:
                print "[%02d bin]" % i_bin
                print "   binCenter from FEWZ output: %lf" % binCenter
                print "   binCenter from customized bin: %lf (%lf - %lf)" % (binCenter_fromCustomBin, list_binEdge[i], list_binEdge[i+1] )
                sys.exit()

            # print "[%02d bin]" % i_bin
            # print "  bin content = %lf\n" % binValue["binContent"]
            # print "  PDFErr      = %lf\n" % binValue["PDFErr"]

            h_ROOT.SetBinContent(i_bin, binValue["binContent"])

            integErr = binValue["integErr"]
            PDFErr = binValue["PDFErr"]
            error = math.sqrt( integErr*integErr + PDFErr*PDFErr )

            h_ROOT.SetBinError(i_bin, error)

            h_ROOT_integErr.SetBinContent(i_bin, integErr)
            h_ROOT_integErr.SetBinError(i_bin, 0)

            h_ROOT_PDFErr.SetBinContent(i_bin, PDFErr)
            h_ROOT_PDFErr.SetBinError(i_bin, 0)

        print "   Successfully converted with customized bin (ROOT histogram name: %s)" % self.dic_histName[FEWZHistName]
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