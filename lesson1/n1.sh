#1/bin/bash
if [ $# = 0 ]; then
	find /home/student/ -maxdepth 1 -type f -size "+10k" -size "-100k" -exec ls -lS {} \; | sort -nk5
else
	if [ "$1" = "-R" ];	then
		find /home/student/ -type f -size "+10k" -size "-100k" -exec ls -lS {} \; | sort -nk5
	fi
fi
echo "This files there are in current directory. For recursive search use -R argument."
