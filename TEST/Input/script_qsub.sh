#!/bin/bash

qsub -l vnode=node5 XSecForDYSample_v00.sh
qsub -l vnode=node1 XSecForDYSample_v01.sh
qsub -l vnode=node2 XSecForDYSample_v02.sh
qsub -l vnode=node3 XSecForDYSample_v03.sh
qsub -l vnode=node4 XSecForDYSample_v04.sh

# qsub -l vnode=node5:ncpus=24 XSecForDYSample_v00.sh
# qsub -l vnode=node1:ncpus=24 XSecForDYSample_v01.sh
# qsub -l vnode=node2:ncpus=24 XSecForDYSample_v02.sh
# qsub -l vnode=node3:ncpus=24 XSecForDYSample_v03.sh
# qsub -l vnode=node4:ncpus=24 XSecForDYSample_v04.sh
