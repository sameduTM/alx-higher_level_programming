#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
if eval "curl -sI $1" | grep -q 'HTTP/1.1 200 OK'; then curl -s -X "GET" $1; fi
