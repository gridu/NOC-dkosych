
#!/bin/bash
echo 'IP in eth0 connection:'
ifconfig | grep -A 1 -e eth0* | grep 'inet addr' |  cut -d':' -f 2 | cut -d' ' -f 1
