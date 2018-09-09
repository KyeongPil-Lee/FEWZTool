#!bin/bash

if [ $FEWZ_PATH ]; then
    echo "KP_ANALYZER_PATH is already defined: use a clean shell!"
    return 1
fi

export FEWZ_PATH=$(pwd)
export PYTHONPATH=${FEWZ_PATH}:${PYTHONPATH}