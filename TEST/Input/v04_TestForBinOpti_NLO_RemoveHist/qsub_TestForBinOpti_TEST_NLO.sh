# -- NOT intended for sourcing ...
# -- (after customization) just copy the commands and type in the terminal

cd /home/kplee/Physics/FEWZ/v03_absRapCut/FEWZ_3.1.rc/bin
qsub -l vnode=node5 TestForBinOpti_TEST_NLO_v00.sh
qsub -l vnode=node5 TestForBinOpti_TEST_NLO_v01.sh
qsub -l vnode=node5 TestForBinOpti_TEST_NLO_v02.sh
qsub -l vnode=node5 TestForBinOpti_TEST_NLO_v03.sh
