# FEWZ calculation for DY reweighting

## Motivation

To produce the NNLO cross sections in 3-dimentions: dilepton (pT, rapidity) in each dilepton mass range

And this result will be used for reweighting NLO DY samples



## Setup

```
git clone git@github.com:KyeongPil-Lee/FEWZTool.git -b v01_Reweighting v01_Reweighting
cd v01_Reweighting

source setup.sh
```



## Cross sections for each DY sample

### Setup

* FSR: off
* dR for dressed lepton: 0.0 (turned off)



## Bin optimization

Check the k-factor distribution with pT-|Y| fine binning in each representative mass ranges

* Mass range: [15, 60], [60, 120], [120, 1000], [1000, 3000]
  * Dilepton pT: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 1000
    * 14 bins
  * Dilepton |rapidity|: 0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 3.0, 100
    * 10 bins
  * FEWZ job: calculate x-section in each |rapidity| bin (with pT histogram): 10 jobs per mass range
    * Total 40 jobs



### Update FEWZ codes to be able to cut on |y(ll)| instead of y(ll)

Modify ```src/constraint.F```

* From

  ```
        if ((Y.lt.ZYmin).or.(Y.gt.ZYmax)) then
           constraint = 0.0d0
           RETURN
        endif
  ```

* To (Y -> dabs(Y))

  ```
        if ((dabs(Y).lt.ZYmin).or.(dabs(Y).gt.ZYmax)) then
           constraint = 0.0d0
           RETURN
        endif
  ```

  * Saved in ```FEWZCodes/constraint.F```
  * Compile again



Modify ```src/histogram.F```

- from ```fillValue(H_ZRAP) = z_Y```
- to ```fillValue(H_ZRAP) = dabs(z_Y)```
- Save in ```FEWZCodes/histogram.F```



Make a new working directory for FEWZ

```
export SCRAM_ARCH=slc6_amd64_gcc630
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

# -- CMSSW enviornment -- #
cd /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_10_1_9 # -- has NNPDF3.1+luxQED PDF set
eval `scramv1 runtime -sh` # -- cmsenv

cd /home/kplee/Physics/FEWZ
mkdir v03_absRapCut; cd v03_absRapCut

wget http://www.hep.anl.gov/fpetriello/FEWZ_3.1.rc.tar.gz
tar -zxvf FEWZ_3.1.rc.tar.gz

cd FEWZ_3.1.rc
```

- Update ```makefile``` to use LHAPDF

  ```
  LHAPDF = on
  LHADIR = /cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/lhapdf/6.2.1-omkpbe3/lib # -- same with $LHAPDF_DATA_PATH/../../lib
  ```

- Copy ```FEWZCodes/constraint.F``` and ```FEWZCodes/histogram.F``` under ```src```

- Compile

  ```
  make fewzz >&make_fewzz.log&
  tail -f make_fewzz.log
  ```



### Job submission plan for 40 jobs

* NLO jobs as a test: 1 day



* NNLO (2.5 days per jobs)
  * 2.5 days * 40 jobs = 100 days
    * 240 cores (10 jobs in parallel): ~10 days
    * 288 cores (12 jobs in parallel): ~8.3 days
  * Available server: total 15 jobs in parallel
    * 3 jobs per 24 cores: 14 jobs in parallel is enough
    * tamsa2: 8 or 12
      * node 4, 6, 7-1, 7-2, 8-1, 8-2, 9-1, 9-2
      * Additionially node 1, 2, 3, 5 will be possible soon
    * muon: 1
    * snu1: 1
    * snu2: 1





### NLO Jobs







## Outdated

### Update FEWZ codes to make |y(ll)| histogram instead of y(ll)

* New FEWZ working directory

  ```
  export SCRAM_ARCH=slc6_amd64_gcc630
  export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
  source $VO_CMS_SW_DIR/cmsset_default.sh
  
  # -- CMSSW enviornment -- #
  cd /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_10_1_9 # -- has NNPDF3.1+luxQED PDF set
  eval `scramv1 runtime -sh` # -- cmsenv
  
  cd /home/kplee/Physics/FEWZ
  mkdir v02_absRap; cd v02_absRap
  
  wget http://www.hep.anl.gov/fpetriello/FEWZ_3.1.rc.tar.gz
  tar -zxvf FEWZ_3.1.rc.tar.gz
  
  cd FEWZ_3.1.rc
  ```

  * Update ```makefile``` to use LHAPDF

    ```
    LHAPDF = on
    LHADIR = /cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/lhapdf/6.2.1-omkpbe3/lib # -- same with $LHAPDF_DATA_PATH/../../lib
    ```

* src/histogram.F

  * from ```fillValue(H_ZRAP) = z_Y```
  * to ```fillValue(H_ZRAP) = dabs(z_Y)```
  * Save in ```FEWZCodes/histogram.F```

* Compile

  ```
  make fewzz >&make_fewzz.log&
  tail -f make_fewzz.log
  ```



## Troubleshootting

### Error at the start of the run

```
At line 15 of file /home/kplee/Physics/FEWZ/v03_absRapCut/FEWZ_3.1.rc/src/histogram.F (unit = 17, file = '../v20181003_TestForBinOpti_TEST_M60to120_diRap5.0to100.0_NLO_hist.txt')
Fortran runtime error: End of file
```

=> Remove '.' in the histogram file name (replace '.' to 'p')



### Negative entry in |y| histogram

Run with 15 < M < 60 GeV, 0 < |y| < 0.3

    -0.15           4.10262         0.0373443          0.045631
     0.15           146.023          0.128338           1.61538
     0.45           4.04479         0.0494971         0.0439707
=> Something wrong?



* Try without any modification on ```src/histogram.F```

  ```
  export SCRAM_ARCH=slc6_amd64_gcc630
  export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
  source $VO_CMS_SW_DIR/cmsset_default.sh
  
  # -- CMSSW enviornment -- #
  cd /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_10_1_9 # -- has NNPDF3.1+luxQED PDF set
  eval `scramv1 runtime -sh` # -- cmsenv
  
  cd /home/kplee/Physics/FEWZ
  mkdir v04_absRapCutOnly; cd v04_absRapCutOnly
  
  wget http://www.hep.anl.gov/fpetriello/FEWZ_3.1.rc.tar.gz
  tar -zxvf FEWZ_3.1.rc.tar.gz
  
  cd FEWZ_3.1.rc
  ```

  - Update ```makefile``` to use LHAPDF

    ```
    LHAPDF = on
    LHADIR = /cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/lhapdf/6.2.1-omkpbe3/lib # -- same with $LHAPDF_DATA_PATH/../../lib
    ```

  - Copy ```FEWZCodes/constraint.F``` under ```src```

  - Compile

    ```
    make fewzz >&make_fewzz.log&
    tail -f make_fewzz.log
    ```

  - Run same job

    ```
    cd bin
    # -- after update to v04_absRapCutOnly path
    qsub -l vnode=node10 v20181002_TestForBinOpti_M15to60_diRap0.0to0.3_NLO.sh
    ```

  - Result

    ```
        -0.45           2.01073          0.030924         0.0218217
        -0.15           75.1358         0.0923192          0.831384
         0.15           74.9902         0.0941544          0.829648
         0.45           2.03826         0.0328891         0.0221983
    ```

    - Cut seems not correctly applied?



* Try with default setup

  ```
  cd /home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc/bin
  # -- after update to v04_absRapCutOnly path
  qsub -l vnode=node5 v20181002_TestForBinOpti_M15to60_diRap0.0to0.3_NLO.sh
  ```






  ### Error in ./finish.sh

  15 < M < 60, 5.0 < |y| < 100.0

  ```
  Traceback (most recent call last):
    File "scripts/do_pdfs.py", line 311, in <module>
      staterrstr = flt2str(staterr)
    File "/home/kplee/Physics/FEWZ/v03_absRapCut/FEWZ_3.1.rc/bin/scripts/defs.py", line 54, in flt2str
      return ( '%g' % fltnum )
  TypeError: float argument required, not str
  job is completed
  
  ```

  * Same error in the other region
    * 5.0 < |y| < 100.0
      * [15, 60], [60, 120], [120, 1000], [1000, 3000]
    * 4.0 < |y| < 5.0
      * [1000, 3000]
    * 3.0 < |y| < 4.0
      - [1000, 3000]
  * It usually happens when PDF replica result has no histogram...



* Check the histogram (1000 < M < 3000 GeV, 5.0 < |Y| < 100.0)

  ```
    ----   A0 vs ZpT      ----
  
       5.00                 0         undefined
      15.00                 0         undefined
      25.00                 0         undefined
      35.00                 0         undefined
      45.00                 0         undefined
      55.00                 0         undefined
      65.00                 0         undefined
      75.00                 0         undefined
      85.00                 0         undefined
      95.00                 0         undefined
  ```

  * Cross section is also 0

    ```
     Sigma (pb)                  =    0.0000000000000000     
     Error (pb)                  =    1.5603705345032397E-020
     chi^2/iteration             =    0.0000000000000000   
    ```

* Another histogram (15 < M < 60 GeV, 5.0 < |Y| < 100.0)

  ```
    ----   A0 vs ZpT      ----
  
       5.00         0.0659615        0.00335303
      15.00          0.523507         0.0120899
      25.00            0.7237          0.027607
      35.00          0.909584         0.0655056
      45.00           1.12059          0.163689
      55.00           1.89576          0.449795
      65.00           1.29071           0.80028
      75.00           1.83424           1.02104
      85.00                 0         undefined
      95.00                 0         undefined
  
  ```

* These "undefined" makes error

* Let's turn-off those histograms & test

  ```
  Keep dilepton & lepton distribution and remote the others
  ```

* Check the result (5.0 < |Y| < 100.0 for each mass range)

  ```
  /home/kplee/Physics/FEWZ/v03_absRapCut/FEWZ_3.1.rc/bin
  ```

  * Finished without errors, but cross section = 0 above M > 120 GeV: need to adjust |Y| bins
  * Let's merge high |Y| bins
    * 3.0, 4.0, 5.0, 100.0 -> 3.0, 100.0
  * 