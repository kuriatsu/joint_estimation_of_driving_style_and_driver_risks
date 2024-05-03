#! /usr/bin/sh

for i in {1..7}; do
    for j in {1..100}; do
        sumo -n sumo/straight.net.xml -r sumo/straight${i}.rou.xml --statistic-output log/straight${i}_stat_${j}.xml
        # sumo -n sumo/straight.net.xml -r sumo/straight${i}.rou.xml --fcd-output log/straight${i}_fcd_${j}.xml --statistic-output log/straight${i}_stat_${j}.xml
    done
done

