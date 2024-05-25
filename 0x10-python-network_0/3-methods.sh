#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI -L -X OPTIONS example.com | grep Allow | cut -c8-
