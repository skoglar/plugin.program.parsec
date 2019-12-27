#!bin/bash

parsec_bin=$1

systemctl stop kodi 
$parsec_bin < data/$opts
wait
echo Finished!
systemctl start kodi