for num in $(cat leftlistsorted)
do 
  rownumber=$((rownumber+1))
  numberinrightlist=$(sed -n "$rownumber"p rightlistsorted)
  if [ $num -gt $numberinrightlist ]; then 
    result=$(($num - $numberinrightlist))
  else 
    result=$(($numberinrightlist - $num))
  fi
  echo $result
done
