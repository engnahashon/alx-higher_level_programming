#!/bin/bash
#  sends a GET request to the URL, and displays the body of the response
response=$(curl -s -w "%{http_code}" $1)

if [ ${response:(-3)} = "200" ]; then
    body=$(curl -s $1)
    echo $body
fi
