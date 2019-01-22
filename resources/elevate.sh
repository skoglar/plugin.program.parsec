#!/bin/sh
DIR="/storage/.kodi/addons/plugin.program.parsec/resources"

if [[ $2 = "first_run" ]]; then
	echo "IM HERE"
	systemd-run $DIR/first_run.sh "$@"
else
	echo "HELLO"
	systemd-run $DIR/run_parsec.sh "$@"
fi