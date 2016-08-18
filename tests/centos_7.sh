#!/bin/sh

DOCKER_OUTPUT=`docker exec -i -t RHEL7-CIS ps aux | grep init`

echo $DOCKER_OUTPUT

if [[ $DOCKER_OUTPUT == *"/usr/sbin/init"* ]];
then
    exit 0;
else
    exit 1;
fi
