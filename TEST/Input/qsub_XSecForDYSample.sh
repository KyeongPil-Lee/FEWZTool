# -- NOT intended for sourcing ...
# -- (after customization) just copy the commands and type in the terminal

cd /home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc/bin
qsub -l vnode=node3 XSecForDYSample_v00.sh
qsub -l vnode=node4 XSecForDYSample_v01.sh
qsub -l vnode=node6 XSecForDYSample_v02.sh
qsub -l vnode=node7 XSecForDYSample_v03.sh
qsub -l vnode=node7 XSecForDYSample_v04.sh
qsub -l vnode=node9 XSecForDYSample_v05.sh
qsub -l vnode=node9 XSecForDYSample_v06.sh

# -- on MUON server
# qsub -l vnode=node9 XSecForDYSample_v07.sh
# -- update FEWZ bin path
source v20181002_XSecForDYSample_M800to1000.sh >&v20181002_XSecForDYSample_M800to1000.log&

qsub -l vnode=node8 XSecForDYSample_v08.sh
qsub -l vnode=node2 XSecForDYSample_v09.sh
qsub -l vnode=node8 XSecForDYSample_v10.sh

# -- below: unsubmitted yet

# -- not urgent
qsub -l vnode=node9 XSecForDYSample_v11.sh
qsub -l vnode=node9 XSecForDYSample_v12.sh
qsub -l vnode=node9 XSecForDYSample_v13.sh
