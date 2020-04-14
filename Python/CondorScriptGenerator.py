import os, sys

class CondorScriptGenerator:
    def __init__(self):

        self.FEWZInputGenerator = ""
        self.FEWZBinPath = ""
        self.WSPath = "" # -- workspace containing all inputs. FEWZ result will also be saved here.

        # -- cmssw environment: for LHAPDF
        self.SCRAM_ARCH = "slc7_amd64_gcc700"
        self.CMSSW_VERSION = "CMSSW_10_6_8"


    def Generate(self):
        self.CopyInputsToFEWZBinPath()
        self.GenerateScript_RunFEWZPerSector()
        self.GenerateCondorScript()

        self.GenerateScript_Finish()

    def GenerateCondorScript(self):
        fileName_script = self.FEWZInputGenerator.MakeFileName( 'script' )
        condorScriptName = "condorScript_" + fileName_script
        condorScriptName = condorScriptName.replace(".sh", ".jds")

        f = open(condorScriptName, "w")
        f.write(
"""

executable = {scriptName_}
universe   = vanilla
log        = condor.log
getenv     = True
should_transfer_files = YES
when_to_transfer_output = ON_EXIT
output = condor_output.log
error  = condor_error.log
accounting_group=group_cms
""".format(scriptName_=fileName_script))

        if self.FEWZInputGenerator.QCDOrder == 2: # -- NNLO calculation
            for i_sector in range(1, 128): # -- from 1 to 127
                f.write("Arguments  = %s\nqueue 1\n\n" % i_sector)
            f.write("\n")

        else: # -- LO or NLO calculation: only 1 sector needed
            f.write("Arguments  = 1\nqueue 1\n\n")

        f.close()

        print "[CondorScriptGenerator] condor script is generated: %s" % condorScriptName
        print "[CondorScriptGenerator] condor submission: "
        print "condor_submit %s\n" % condorScriptName


    def GenerateScript_RunFEWZPerSector(self):
        fileName_param  = self.FEWZInputGenerator.MakeFileName( 'param' )
        fileName_hist   = self.FEWZInputGenerator.MakeFileName( 'hist' )
        fileName_output = self.FEWZInputGenerator.MakeFileName( 'output' )
        dirName         = self.FEWZInputGenerator.MakeFileName( 'dir' )
        nCPU = self.FEWZInputGenerator.nCore

        orderName = "LO"
        if   self.FEWZInputGenerator.QCDOrder == 1: orderName = "NLO"
        elif self.FEWZInputGenerator.QCDOrder == 2: orderName = "NNLO"

        fileName_script = self.FEWZInputGenerator.MakeFileName( 'script' )
        f = open(fileName_script, "w")
        f.write(
"""#!/bin/bash

# -- script for FEWZ calculation per sector
# -- usage: source <script name> <sector number> (1 for LO & NLO; 1-127 for NNLO)

SectorNum=$1
echo 'Arg: SectorNum = '$SectorNum

start=`date +%s`

export SCRAM_ARCH={SCRAM_ARCH_}
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

# -- CMSSW enviornment -- #
cd /cvmfs/cms.cern.ch/{SCRAM_ARCH_}/cms/cmssw/{CMSSW_VERSION_} # -- has NNPDF3.1+luxQED PDF set
eval `scramv1 runtime -sh` # -- cmsenv

cd {FEWZBinPath_}

echo "run local_run.sh"
./local_run.sh z \\
{dirName_} \\
{fileName_param_} \\
{fileName_hist_} \\
{fileName_output_} \\
../ \\
{nCore_} \\
$SectorNum

end=`date +%s`

runtime=$((end-start))
runtime_m=`echo "$runtime/60.0"|bc`
runtime_h=`echo "$runtime_m/60.0"|bc`

echo "   start:   "$start
echo "   end:     "$end
echo "   runtime: "$runtime" (second) = "$runtime_m" (min) = "$runtime_h" (hour)"

""".format(SCRAM_ARCH_=self.SCRAM_ARCH, CMSSW_VERSION_=self.CMSSW_VERSION, FEWZBinPath_=self.FEWZBinPath,
    dirName_=dirName, fileName_param_=fileName_param, fileName_hist_=fileName_hist, fileName_output_=fileName_output,
    nCore_=nCPU))

        f.close()

        print "[CondorScriptGenerator] script for local_run.sh is generated: %s" % fileName_script


    def GenerateScript_Finish(self):
        fileName_script = self.FEWZInputGenerator.MakeFileName( 'script' )
        fileName_script = fileName_script.replace(".sh", "_finish.sh")

        dirName         = self.FEWZInputGenerator.MakeFileName( 'dir' )
        fileName_output = self.FEWZInputGenerator.MakeFileName( 'output' )

        orderName = "LO"
        if   self.FEWZInputGenerator.QCDOrder == 1: orderName = "NLO"
        elif self.FEWZInputGenerator.QCDOrder == 2: orderName = "NNLO"

        f = open(fileName_script, "w")
        f.write(
"""#!/bin/bash

cwd=$(pwd)

cd {FEWZBinPath_}

echo "run finish.sh"
./finish.sh \\
{dirName_} \\
{orderName_}.{fileName_output_}

# -- bring the output .dat file to Workspace
cp {orderName_}.{fileName_output_} {WSPath_}

cd $cwd

echo "job is completed"

""".format(dirName_=dirName, orderName_=orderName, fileName_output_=fileName_output, 
    FEWZBinPath_=self.FEWZBinPath, WSPath_=self.WSPath))

        f.close()

        print "[CondorScriptGenerator] script for finish.sh is generated: %s" % fileName_script
        print " ---> Run after all condor jobs per sector are finished"


    # -- always copy: overwrite if a file exists with same name under self.FEWZBinPath
    def CopyInputsToFEWZBinPath(self):
        fileName_param = self.FEWZInputGenerator.MakeFileName( 'param' )
        fileName_hist = self.FEWZInputGenerator.MakeFileName( 'hist' )
        # fileName_output = self.FEWZInputGenerator.MakeFileName( 'output' )
        # dirName = self.FEWZInputGenerator.MakeFileName( 'dir' )

        cmd_cp = "cp %s %s" % (fileName_param, self.FEWZBinPath)
        os.system( cmd_cp )
        print "[CondorScriptGenerator] Copy: %s\n -> %s/%s" % (fileName_param, self.FEWZBinPath, fileName_param)

        cmd_cp = "cp %s %s" % (fileName_hist, self.FEWZBinPath)
        os.system( cmd_cp )
        print "[CondorScriptGenerator] Copy: %s\n -> %s/%s" % (fileName_hist, self.FEWZBinPath, fileName_hist)

        if len(self.FEWZInputGenerator.list_binTextFile) > 0:
            for binTextFile in self.FEWZInputGenerator.list_binTextFile:
                cmd_cp = "cp %s %s" % (binTextFile, self.FEWZBinPath)
                os.system( cmd_cp )
                print "[CondorScriptGenerator] Copy: %s\n -> %s/%s" % (binTextFile, self.FEWZBinPath, binTextFile)

        print "\n"
