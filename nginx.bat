@echo off
ipconfig | find /I "ipv4"
netsh wlan set hostednetwork mode=allow ssid="LandRover21" key="toolongkey" keyUsage=persistent
netsh wlan start hostednetwork
echo "launch nginx.exe background"
start /b nginx.exe
echo "launch python django web server"
python "D:\handson\python\pandora\manage.py" runserver 10.33.55.1:80
