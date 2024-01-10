#!/bin/bash

SERVICE_FILE=/etc/systemd/system/balanceWrite.service
TIME_FILE=/etc/systemd/system/balanceWrite.timer

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'
NEED_RELOAD_DAEMON=false

function createServiceFile() {
echo "[Unit]
Description=DiscordBot write balance exp

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /root/DiscordBot/firstVDSInfo/main.py

[Install]
WantedBy=multi-user.target" > $SERVICE_FILE

NEED_RELOAD_DAEMON=true
}

function createTimerFile() {
echo "[Unit]
Description=balanceWrite timer
Requires=balanceWrite.service

[Timer]
OnCalendar=*-*-* 05:00:00
Unit=balanceWrite.service
AccuracySec=1us

[Install]
WantedBy=timers.target" > $TIME_FILE

NEED_RELOAD_DAEMON=true
}

if [ ! -f $SERVICE_FILE ]; then
    createServiceFile
    echo -e "${GREEN}[OK]${NC} FILE $SERVICE_FILE CREATED!"
else
   echo -e "${RED}[ERROR]${NC} FILE $SERVICE_FILE EXISTS!"
fi

if [ ! -f $TIME_FILE ]; then
    createTimerFile
    echo -e "${GREEN}[OK]${NC} FILE $TIME_FILE CREATED!"
else
   echo -e "${RED}[ERROR]${NC} FILE $TIME_FILE EXISTS!"
fi

if $NEED_RELOAD_DAEMON; then
    echo "RELOAD DAEMON"
    systemctl daemon-reload
    echo "START TIMER"
    systemctl start balanceWrite.timer
fi
