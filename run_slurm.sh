#!/bin/bash

export NAME=DC

export EXECUTOR="sbatch --out=/dev/null --exclude=rome0[1-3],dhabi0[1-3],naples0[1-3],vmware0[1-4] --partition=cpu -n1 --mem=16G "
./run_$NAME.sh
