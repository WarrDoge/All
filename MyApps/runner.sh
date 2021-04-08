#!/bin/bash
SERVICE="x.py"
if pgrep -f "/root/$SERVICE" >/dev/null 2>&1 ; then
    echo "$SERVICE is running"
else     
	nohup python3 x.py &
fi