#!/bin/bash

CUR=$(pwd)
DIR="experiment/$NAME/AV${AGENT_V}_AP${AGENT_P}_GV${GV}_GP${GP}_R${RUNS}"
mkdir -p $DIR
cd $DIR
echo "$DIR"

$EXECUTOR $CUR/uppaal-5.0.0-rc2-linux64/bin/verifyta -s --good-runs $RUNS --total-runs $RUNS --max-iterations 1 --eval-runs 1 -D 0.1 $CUR/models/${NAME}_Partitioned.xml &> out
