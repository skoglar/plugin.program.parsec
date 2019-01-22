#!bin/bash

parsec_bin=$1
opts="server_id=$2"

systemctl stop kodi 
$parsec_bin $opts
wait
echo Finished!
systemctl start kodi