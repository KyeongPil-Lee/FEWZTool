# -- NOT intended for sourcing ...
# -- (after customization) just copy the commands and type in the terminal

cd /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v09_HighMass
qsub -l ncpus=8 v20181031_DYReweight_HighMass_v00.sh
qsub -l ncpus=8 v20181031_DYReweight_HighMass_v01.sh
qsub -l ncpus=8 v20181031_DYReweight_HighMass_v02.sh
