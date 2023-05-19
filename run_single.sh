#!/bin/bash

CUR=$(pwd)

if [[ $NAME == DC ]] ; then
    DIR="raw/$EXPNAME/$NAME/AI${AGENT_I}_AV${AGENT_V}_AR${AGENT_R}_GI${GRID_I}_GV${GRID_V}_GR${GRID_R}_R${RUNS}_C${SAMPLED_COST}"
elif [[ $NAME == BB ]] ; then
    DIR="raw/$NAME/AV${AGENT_V}_AP${AGENT_P}_GV${GRID_V}_GP${GRID_P}_R${RUNS}_C${SAMPLED_COST}"
else
    echo "unexpected value NAME (was: $($NAME))"
    exit 1
fi

mkdir -p $DIR
cd $DIR
echo "$DIR"

#R=$( /usr/bin/time -v $CUR/uppaal-5.0.0-rc2-linux64/bin/verifyta.sh -s --good-runs $RUNS --total-runs $RUNS --max-iterations 1 --eval-runs 1 -D 0.05 $CUR/models/${NAME}_partitioned.xml 2>&1)
R=$( /usr/bin/time -v $CUR/$UPPAAL/verifyta.sh --random-search-limit 1 --deterministic-search-limit 1 -s --good-runs $RUNS --total-runs $RUNS --max-iterations 1 --eval-runs 1 -D 0.05 $CUR/models/${NAME}_partitioned.xml 2>&1)

echo "$R" > out
