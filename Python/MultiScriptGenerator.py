import sys

class MultiScriptGenerator:
    def __init__(self):
        self.tag = ""
        self.FEWZBinPath = ""
        self.list_scriptName = []
        self.nJobPerScript = 0

        # -- internal variable
        self.nTotalJob = 0
        self.list_subScriptName = []

    def Generate(self):
        self.CheckOptions()

        nScript = len(self.list_scriptName)
        self.nTotalJob = self.Ceiling( float(nScript) / float(self.nJobPerScript) )
        print "nScript = %d, nJobPerScript = %d -> nTotalJob: %d" % (nScript, self.nJobPerScript, self.nTotalJob)

        self.GenerateScript()


    def GenerateScript(self):
        for i in range(0, self.nTotalJob):
            self.GenerateSubScriptPerJob(i)

        self.GenerateQsubScript()

    def GenerateSubScriptPerJob(self, i):
        list_filePerJob = []
        if i == self.nTotalJob-1:
            list_filePerJob = self.list_scriptName[int(i*self.nJobPerScript):]
        else:
            list_filePerJob = self.list_scriptName[int(i*self.nJobPerScript):int((i+1)*self.nJobPerScript)]

        subScriptName = "%s_v%02d.sh" % (self.tag, i)
        f = open(subScriptName, "w")

        f.write("#!/bin/bash\n\n")

        cmd_cd = "cd %s" % self.FEWZBinPath
        f.write(cmd_cd+"\n\n")

        for fileName in list_filePerJob:
            cmd = "source %s >&%s.log" % (fileName, fileName.split(".sh")[0])
            f.write(cmd+"\n")
            cmd_echo = 'echo "%s: finished"' % fileName
            f.write(cmd_echo+"\n\n")

        f.write("\n")
        f.write('echo "ALL: finished"\n')
        f.close()

        print "%s is generated" % subScriptName
        self.list_subScriptName.append(subScriptName)

    def GenerateQsubScript(self):
        qsubScriptName = "qsub_%s.sh" % self.tag

        f = open(qsubScriptName, "w")
        f.write("# -- NOT intended for sourcing ...\n")
        f.write("# -- (after customization) just copy the commands and type in the terminal\n\n");

        f.write("cd %s\n" % self.FEWZBinPath)

        for subScriptName in self.list_subScriptName:
            cmd = "qsub %s\n" % subScriptName
            f.write(cmd)

        print "%s is generated" % qsubScriptName
        f.close()


    def CheckOptions(self):
        if self.tag == "":
            print "no tag!"
            sys.exit()

        if self.FEWZBinPath == "":
            print "no FEWZBinPath!"
            sys.exit()

        if len(self.list_scriptName) == 0:
            print "No input list of script names"
            sys.exit()

        if self.nJobPerScript == 0:
            print "nJobPerScript == 0"
            sys.exit()

    def Ceiling( self, value ):
        if value > int(value):
            return int(value+1)
        else:
            return int(value)

