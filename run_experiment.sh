#!/bin/bash

export NAME=BB

for RUNS in 100 1000 5000 10000 25000 ; do
    for NGRID in $(seq 1 10 1000) ; do 
        for AGENT_V in -1 0 1 2; do
            for AGENT_P in -1 0 1 2 ; do
                export AGENT_V=$AGENT_V
                export AGENT_P=$AGENT_P
                export GRID_P=$NGRID
                export GRID_V=$(($NGRID*2))
                export RUNS=$RUNS
                ./run_single.sh
            done
        done
    done
done
