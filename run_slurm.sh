#!/bin/bash

export EXECUTOR="srun --partiton=rome -n1 --mem=1G "
./run_experiment.sh
