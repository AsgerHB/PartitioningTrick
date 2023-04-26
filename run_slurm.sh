#!/bin/bash

export EXECUTOR="sbatch --out=/dev/null --partition=rome -n1 --mem=1G "
./run_experiment.sh
