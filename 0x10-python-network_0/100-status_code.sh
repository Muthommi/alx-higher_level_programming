#!/bin/bash
# A script that sends a request to a URL passed as an argument

if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

curl -s -o /dev/null -w "%{http_code}" "$1"
