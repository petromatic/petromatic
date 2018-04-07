#!/usr/bin/env bash

if [ ! -z "$1" ]; then
	echo $(echo $(dmesg | grep ttyUSB | grep attached | grep $1) | awk 'NF>1{print $NF}');
else
	echo "FLOWMETER" $(echo $(dmesg | grep ttyUSB | grep attached | grep cp210x) | awk 'NF>1{print $NF}');
	echo "LR" $(echo $(dmesg | grep ttyUSB | grep attached | grep ch341) | awk 'NF>1{print $NF}');
	echo "EM" $(echo $(dmesg | grep ttyUSB | grep attached | grep pl2303) | awk 'NF>1{print $NF}');
fi
