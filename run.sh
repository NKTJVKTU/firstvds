#!/bin/bash

SERVICE_FILE=/etc/systemd/system/balanceWrite.service
TIME_FILE=/etc/systemd/system/balanceWrite.timer

if [ ! -f $SERVICE_FILE ]; then
    touch $SERVICE_FILE
fi

echo "[Unit]
Description=DiscordBot write balance exp

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /root/DiscordBot/firstVDSInfo/main.py

[Install]
WantedBy=multi-user.target" > $SERVICE_FILE

echo "[Unit]
Description=balanceWrite timer
Requires=balanceWrite.service

[Timer]
OnCalendar=*-*-* 01:00:00
Unit=balanceWrite.service
AccuracySec=1us

[Install]
WantedBy=timers.target" > $TIME_FILE

systemctl daemon-reload
systemctl start balanceWrite.timer
