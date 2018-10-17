# -- NOT intended for sourcing ...
# -- (after customization) just copy the commands and type in the terminal

cd /data9/Users/kplee/FEWZTool/v02_LowMass/Workspace/v01
qsub -l ncpus=24 LowMassTest_v00.sh
qsub -l ncpus=24 LowMassTest_v01.sh
