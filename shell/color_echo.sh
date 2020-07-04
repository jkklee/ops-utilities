#!/bin/sh
# by ljk
if [[ $1 == "-n" ]];then
    n=$1
    color=$2
    shift 2    
else
    color=$1
    shift 1
fi
case $color in
    'green')
        echo $n -e "\033[32m$*\033[0m";;
    'yellow')
        echo $n -e "\033[33m$*\033[0m";;
    'blue')
        echo $n -e "\033[36m$*\033[0m";;
    'purple')
        echo $n -e "\033[35m$*\033[0m";;
    'red')
        echo $n -e "\033[31m$*\033[0m";;
    *)
        echo $n -e "$*";;
esac
