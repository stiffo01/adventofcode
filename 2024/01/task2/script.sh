#!/bin/bash
for num in $(cat leftlistsorted)
do
  result=$(grep "$num" rightlistsorted | uniq -c | sed 's/^ *//g' | cut -d" " -f1)
  if [ -n "$result" ]; then
    result=$(( $num * $result ))
    final=$(( $final + $result ))
    echo $final
  fi
done 
