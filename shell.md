## Service SystemD
```
nano /etc/systemd/system/balanceWrite.service
```
```
[Unit]
Description=DiscordBot write balance exp

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /root/DiscordBot/firstVDSInfo/main.py

[Install]
WantedBy=multi-user.target
```

## Timer SystemD
```
nano /etc/systemd/system/balanceWrite.timer
```
```
[Unit]
Description=balanceWrite timer
Requires=balanceWrite.service

[Timer]
OnCalendar=*-*-* 01:00:00
Unit=balanceWrite.service
AccuracySec=1us

[Install]
WantedBy=timers.target
```
```
* sudo systemctl daemon-reload
* systemctl start balanceWrite.timer
```
