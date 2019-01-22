#!/bin/sh
DIR="/storage/.kodi/addons/plugin.program.parsec/resources"

if [[ $2 = "first_run" ]]; then
	systemd-run $DIR/first_run.sh "$@"
else
	systemd-run $DIR/run_parsec.sh "$@"
fi