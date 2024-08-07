#!/bin/bash
# A script that takes in a URL, sends a GET request to the URL with a header.
curl -sH "X-School-User-Id: 98" "$1"
