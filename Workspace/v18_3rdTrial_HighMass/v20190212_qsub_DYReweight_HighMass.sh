# -- NOT intended for sourcing ...
# -- (after customization) just copy the commands and type in the terminal

cd /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v18_3rdTrial_HighMass
qsub -l ncpus=8 v20190212_DYReweight_HighMass_v00.sh
qsub -l ncpus=8 v20190212_DYReweight_HighMass_v01.sh
qsub -l ncpus=8 v20190212_DYReweight_HighMass_v02.sh
