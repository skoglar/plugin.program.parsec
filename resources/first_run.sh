#!bin/bash
data_path=$1
parsec_bin=$1"/parsec"
creds_file=$1"/creds"

systemctl stop kodi
$parsec_bin < $creds_file
wait
echo Finished!
systemctl start kodi