#!/usr/bin/env bash
#
# date: 2019/10/31
# author by hlions
# usage by monitor cpu and memory and disk


US=$(vmstat | awk 'NR==3{ print $13 }')
SY=$(vmstat | awk 'NR==3{ print $14 }')
# shellcheck disable=SC2034
cpu=$((${US}+${SY}))

TOTAL=$(free -mw | awk 'NR==2{ print $2 }')
USE=$(free -mw | awk 'BEGIN{ FS=" " }NR==2{ print $3 }')
CACHE=$(free -mw | awk 'BEGIN{ FS=" " }NR==2{ print $7 }')
# shellcheck disable=SC2034
memory=$(echo "((${USE}+${CACHE})/${TOTAL})*100" | bc -ql)

# shellcheck disable=SC2034
disk=$(df -Th | awk 'NR==2{ print $6 }' | awk -F% '{ print $1 }')

if [ ! -d /monitor ];then
  mkdir "/monitor"
fi
echo "{\"cpu\":${cpu}, \"memory\":${memory}, \"disk\":${disk}}" >>/monitor/info.json
