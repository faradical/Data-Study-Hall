#!/bin/bash

ME=$(whoami)

folders=$(ls /c/Users/$ME/Downloads/ | grep "geckodriver")
for folder in $folders
do
    if [[ ${folder} != *".zip"* ]]; then
        echo "$folder"
        location=$folder
    fi
done

mkdir /c/Users/$ME/webdrivers_ex

cp /c/Users/$ME/Downloads/$location /c/Users/$ME/webdrivers_ex/

PATH=$PATH:/c/Users/$ME/webdrivers_ex/

echo $PATH
