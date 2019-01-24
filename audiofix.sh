#Create alsa config file to connect to pa
printf "pcm.pulse {    type pulse\n}\nctl.pulse {    type pulse\n}\n" > /storage/.config/asound.conf
#remount /flash partition in read-write mode
mount -o remount rw /flash/
#append dtparam=audio=on to config.txt
printf "\n#LE: ACTIVATE ALSA:\ndtparam=audio=on\n" >> /flash/config.txt
