#!/bin/bash
DATE=$(date +"%d-%m-%Y-%H-%M")

#Check for pre-existing directory

if [ -d /tmp/${USER} ]; then
    echo "Directory Already exists!"
else
    echo "Creating Directory /tmp/${USER}..."
    mkdir /tmp/${USER}
fi

#Creating date timestamp based log file
echo "Creating ${DATE}.log  file..."
touch /tmp/${USER}/${DATE}.log

