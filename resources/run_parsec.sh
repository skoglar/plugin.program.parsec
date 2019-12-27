#!bin/bash

parsec_bin=$1
settings_file=$2

systemctl stop kodi 
$parsec_bin < $settings_file
wait
echo Finished!
systemctl start kodi