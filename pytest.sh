#!/bin/sh

echo "\033[1;32m"
cat << "EOF"
Empty
EOF
echo "\033[1;37m"

export CONNECTION_KEY="Im a connection_key"
export PRIVATE_KEY="Im a private_key"
echo $CONNECTION_KEY
echo $PRIVATE_KEY

pytest -s -v
