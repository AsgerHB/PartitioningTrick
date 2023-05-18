#!/bin/bash

export NAME=BB
export UPPAAL=uppaal-rqvar/

for RUNS in 10000 ; do # 5000 10000 25000 50000 100000 250000 500000 ; do
    export RUNS=$RUNS
    for NGRID in $(seq 15 30 1500) ; do 
	export GRID_P=$NGRID
	export GRID_V=$(($NGRID*2))

	# Uniform + sampled cost
	export SAMPLED_COST=2
	export AGENT_V=2
	export AGENT_P=2
    $EXECUTOR ./run_single.sh

	# Historical + sampled cost
	export SAMPLED_COST=2
	export AGENT_V=3
	export AGENT_P=3
    $EXECUTOR ./run_single.sh

	# Best + sampled cost
	# export SAMPLED_COST=2
	# export AGENT_V=-3
	# export AGENT_P=1
    # $EXECUTOR ./run_single.sh

	# Worst + sampled cost
	# export SAMPLED_COST=2
	# export AGENT_V=-2
	# export AGENT_P=-1
    # $EXECUTOR ./run_single.sh

	# Best + best cost
	export SAMPLED_COST=1
	export AGENT_V=-3
	export AGENT_P=1
    $EXECUTOR ./run_single.sh

	# Worst + worst cost
	export SAMPLED_COST=-1
	export AGENT_V=-2
	export AGENT_P=-1
    $EXECUTOR ./run_single.sh


	# Uniform + static cost
	export SAMPLED_COST=0
	export AGENT_V=2
	export AGENT_P=2
    $EXECUTOR ./run_single.sh

	# for AGENT_P in -1 1 ; do
    #         for AGENT_V in -1 1 2 ; do
	# 	# same SAMPLE_COST as AGENT_P
	# 	export SAMPLED_COST=$AGENT_P
    #             export AGENT_V=$AGENT_V
    #             export AGENT_P=$AGENT_P
    #             $EXECUTOR ./run_single.sh
    #         done
    #     done
    # done
done
