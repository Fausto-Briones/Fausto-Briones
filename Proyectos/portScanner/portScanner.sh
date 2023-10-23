#!/bin/bash

ip = '172.18.0.1'

for i in $(seq 1 65535); do
	value = '$(nc -zvn $ip $i | grep open)'
	echo -e "$value\n"
done


