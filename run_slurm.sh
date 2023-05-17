#!/bin/bash

export EXECUTOR="sbatch --out=/dev/null --partition=naples -n1 --mem=16G "
./run_experiment.sh
