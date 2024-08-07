#!/bin/bash
# A script that takes and sends a request to the URL.
curl -s "$1" | wc -c
