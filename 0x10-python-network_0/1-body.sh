#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -GET $1 | grep -v 301
