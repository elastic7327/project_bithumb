#!/bin/sh

echo "\033[1;32m"
cat << "EOF"
 _     _                 _
| |   (_)  _            (_)
| |__  _ _| |_ ____ ___  _ ____
|  _ \| (_   _) ___) _ \| |  _ \
| |_) ) | | |( (__| |_| | | | | |
|____/|_|  \__)____)___/|_|_| |_| - by daniel k

EOF
echo "\033[1;37m"

# 이부분은 적절하게 키값을 넣어주면 됩니다.
# export CONNECTION_KEY="Im a connection_key"
# export PRIVATE_KEY="Im a private_key"
echo $CONNECTION_KEY
echo $PRIVATE_KEY

pytest -s -v --cov=src --cov coveralls  --cov-report html
