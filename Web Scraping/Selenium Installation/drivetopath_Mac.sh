#!/bin/bash

ME=$(whoami)

folders=$(ls /Users/$ME/Downloads/ | grep "geckodriver")
for folder in $folders
do
    if [[ ${folder} != *".gz"* ]]; then
        echo "$folder"
        location=$folder
    fi
done

mkdir /Users/$ME/webdrivers_ex

cp /Users/$ME/Downloads/$location /Users/$ME/webdrivers_ex/

PATH=$PATH:/Users/$ME/webdrivers_ex/

echo $PATH
