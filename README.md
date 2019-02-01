# Tool for FEWZ

## Purpose of this branch

To produce NNLO distribution (cross section) for single lepton eta & dimuon rapidity

* To investigate the discrepancy between the data and MC in high eta region

### Condition

* Z peak region
* Fiducial phase space
* Various PDF sets



### FEWZ installation

* FEWZ 3.1 tar.gz file: [link](http://gate.hep.anl.gov/fpetriello/FEWZ.html) (need to check the latest version first!)

```
export SCRAM_ARCH=slc6_amd64_gcc630
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

# -- CMSSW enviornment -- #
cd /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_10_1_9 # -- has NNPDF3.1+luxQED PDF set
eval `scramv1 runtime -sh` # -- cmsenv

cd ~/Physics/FEWZ/LHAPDF_621
wget http://www.hep.anl.gov/fpetriello/FEWZ_3.1.rc.tar.gz
tar -zxvf FEWZ_3.1.rc.tar.gz

cd FEWZ_3.1.rc

```

* Update ```makefile``` to use LHAPDF

```
LHAPDF = on
LHADIR = /cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/lhapdf/6.2.1-omkpbe3/lib # -- same with $LHAPDF_DATA_PATH/../../lib
```

* Compile

```
make fewzz >&make_fewzz.log&
tail -f make_fewzz.log
```



## Generate FEWZ inputs

```
git clone git@github.com:KyeongPil-Lee/FEWZTool.git
cd FEWZTool
source setup.sh

cd Example
python InputGenerator_example.py
```
