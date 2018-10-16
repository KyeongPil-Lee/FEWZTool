# -- NOT intended for sourcing ...
# -- (after customization) just copy the commands and type in the terminal

cd /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v03_TestForBinOpti_NNLO
qsub -l vnode=node1 TestForBinOpti_v00.sh
qsub -l vnode=node2 TestForBinOpti_v01.sh
qsub -l vnode=node3 TestForBinOpti_v02.sh
qsub -l vnode=node4 TestForBinOpti_v03.sh
qsub -l vnode=node5 TestForBinOpti_v04.sh
qsub -l vnode=node6 TestForBinOpti_v05.sh
qsub -l vnode=node7 TestForBinOpti_v06.sh
qsub -l vnode=node7 TestForBinOpti_v07.sh
qsub -l vnode=node8 TestForBinOpti_v08.sh
qsub -l vnode=node8 TestForBinOpti_v09.sh
qsub -l vnode=node9 TestForBinOpti_v10.sh
qsub -l vnode=node9 TestForBinOpti_v11.sh
