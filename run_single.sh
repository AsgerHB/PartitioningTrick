#!/bin/bash

CUR=$(pwd)
DIR="raw/$EXPNAME/$NAME/AV${AGENT_V}_AP${AGENT_P}_GV${GRID_V}_GP${GRID_P}_R${RUNS}_C${SAMPLED_COST}"
mkdir -p $DIR
cd $DIR
echo "$DIR"

#R=$( /usr/bin/time -v $CUR/uppaal-5.0.0-rc2-linux64/bin/verifyta.sh -s --good-runs $RUNS --total-runs $RUNS --max-iterations 1 --eval-runs 1 -D 0.05 $CUR/models/${NAME}_partitioned.xml 2>&1)
R=$( /usr/bin/time -v $CUR/$UPPAAL/verifyta.sh --random-search-limit 1 --deterministic-search-limit 1 --qlearning-alpha 120000000 -s --good-runs $RUNS --total-runs $RUNS --max-iterations 1 --eval-runs 1 -D 0.05 $CUR/models/${NAME}_partitioned.xml 2>&1)

echo "$R" > out
