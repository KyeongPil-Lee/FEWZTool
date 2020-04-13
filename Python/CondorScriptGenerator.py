import sys

class CondorScriptGenerator:
    def __init__(self):
        self.list_scriptName = []
        self.nCore = 0


    def Generate(self):
        self.CheckOptions()

        list_condorScriptName = []

        for i in range(0, len(self.list_scriptName)):
            condorScriptName = self.GenerateCondorScript(i)
            list_condorScriptName.append( condorScriptName )


        self.GenerateScript_SubmitAll(list_condorScriptName)


    def GenerateCondorScript(self, index):
        condorScriptName = "condorScript_submit_%d.jds" % index

        f = open(condorScriptName, "w")
        f.write(
"""

executable = {scriptName_}
universe   = vanilla
log        = condor_{index_}.log
getenv     = True
should_transfer_files = YES
when_to_transfer_output = ON_EXIT
output = condor_output_{index_}.log
error  = condor_error_{index_}.log
accounting_group=group_cms
RequestCpus = {nCore_}

queue 1

""".format(scriptName_=self.list_scriptName[index], index_=index, nCore_=self.nCore))

        f.close()

        return condorScriptName


    def GenerateScript_SubmitAll(self, list_condorScriptName):
        f = open("script_condorSubmit_all.sh", "w")

        f.write("#!/bin/bash\n")

        for condorScriptName in list_condorScriptName:
            f.write("condor_submit %s" % condorScriptName)

        f.write('\necho "[script_condorSubmit_all.sh] submission: done"\n')

        print "\n[CondorScriptGenerator] Submit all condor jobs: "
        print "source script_condorSubmit_all.sh"
        print ""
        
        f.close()


    def CheckOptions(self):
        if self.nCore < 1:
            print "nCore = %d ... need to be set properly" % self.nCore
            sys.exit()