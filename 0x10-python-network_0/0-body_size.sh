#!/bin/bash
# displays the size of the body of the response
echo "$(curl -s -w "%{size_download}" -o /dev/null "$1")"
