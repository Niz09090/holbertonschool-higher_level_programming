#!/bin/bash
# Display the size of the body of a response in bytes
curl -s -o /dev/null -w "%{size_download}" "$1"
