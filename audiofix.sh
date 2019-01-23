printf "pcm.pulse {    type pulse\n}\nctl.pulse {    type pulse\n}\n" > /storage/.config/asound.conf
mount -o remount rw /flash/
printf "\n#LE: DEACTIVATE ALSA:\ndtparam=audio=on\n" >> /flash/config.txt