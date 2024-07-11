#!/bin/bash
# A script that takes in a URL sends a GET request to the URL.
curl -sL -w "%{http_code}" "$1" -o temp_response | grep -q "200" && cat temp_response
