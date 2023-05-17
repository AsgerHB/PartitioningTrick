#!/bin/bash

export NAME=DC

export EXECUTOR="sbatch --out=/dev/null --partition=dhabi -n1 --mem=16G "
./run_$NAME.sh
