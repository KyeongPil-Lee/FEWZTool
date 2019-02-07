#!/bin/bash

qsub -l ncpus=1 v20190206_FiducialXSec_Zpeak_NNPDF31_nlo_as_0118_NLO.sh
qsub -l ncpus=1 v20190206_FiducialXSec_Zpeak_CT14nlo_as_0118_NLO.sh
