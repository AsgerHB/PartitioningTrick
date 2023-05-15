#!/bin/bash

export EXECUTOR="sbatch --out=/dev/null --partition=cpu -n1 --mem=16G "
./run_experiment.sh
