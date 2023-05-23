#!/bin/bash

export NAME=DC
export UPPAAL=uppaal-rqvar/

for RUNS in 50000 ; do # 5000 10000 25000 50000 100000 250000 500000 ; do
    export RUNS=$RUNS
    for NGRID in $(seq 15 15 1500) ; do 
        export GRID_I=$NGRID
        export GRID_V=$NGRID
        export GRID_R=$NGRID

        # Uniform + sampled cost
        export SAMPLED_COST=2
        export AGENT_I=2
        export AGENT_V=2
        export AGENT_R=2
        $EXECUTOR ./run_single.sh

        # # Historical + sampled cost
        # export SAMPLED_COST=2
        # export AGENT_I=3
        # export AGENT_V=3
        # export AGENT_R=3
        # $EXECUTOR ./run_single.sh

        # # Best + sampled cost
        # export SAMPLED_COST=2
        # export AGENT_I=-3
        # export AGENT_V=-3
        # export AGENT_R=-3
        # $EXECUTOR ./run_single.sh

        # # Worst + sampled cost
        # export SAMPLED_COST=2
        # export AGENT_I=-2
        # export AGENT_V=-2
        # export AGENT_R=-2
        # $EXECUTOR ./run_single.sh

        # Best + best cost
        export SAMPLED_COST=1
        export AGENT_I=-3
        export AGENT_V=-3
        export AGENT_R=-3
        $EXECUTOR ./run_single.sh

        # Worst + worst cost
        export SAMPLED_COST=-1
        export AGENT_I=-2
        export AGENT_V=-2
        export AGENT_R=-2
        $EXECUTOR ./run_single.sh

        # Uniform + static cost
        export SAMPLED_COST=0
        export AGENT_I=2
        export AGENT_V=2
        export AGENT_R=2
        $EXECUTOR ./run_single.sh

        # Lower+worst cost
        export SAMPLED_COST=-1
        export AGENT_I=-1
        export AGENT_V=-1
        export AGENT_R=-1
        $EXECUTOR ./run_single.sh

        # Upper+best cost
        export SAMPLED_COST=1
        export AGENT_I=1
        export AGENT_V=1
        export AGENT_R=1
        $EXECUTOR ./run_single.sh

        # for AGENT_I in -1 1 ; do
        #     for AGENT_V in -1 1 ; do
        #         for AGENT_R in -1 1 ; do
        #             export SAMPLED_COST=0
        #             export AGENT_I=$AGENT_I
        #             export AGENT_V=$AGENT_V
        #             export AGENT_R=$AGENT_R
        #             $EXECUTOR ./run_single.sh
        #         done
        #     done
        # done
    done
done
