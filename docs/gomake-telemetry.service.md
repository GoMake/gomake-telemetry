Create service config file:
```
sudo nano /lib/systemd/system/gomake-telemetry.service
```

*/lib/systemd/system/gomake-telemetry.service* contents:
```
[Unit]
Description=goMake Telemetry Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python /opt/gomake-telemetry/
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

Set run permissions of service:
```
sudo chmod 644 /lib/systemd/system/gomake-telemetry.service
```

Enable service:
```
sudo systemctl daemon-reload
sudo systemctl enable gomake-telemetry.service
```

Reboot to take effect:
```
sudo reboot
```

Systemd Reference: [link](https://medium.com/@johannes_gehrs/getting-started-with-systemd-on-debian-jessie-e024758ca63d)