#!/bin/bash
hosts=$(cat ../env/hosts |egrep '[0-9]'|awk '{print $1}')

function foo(){
for x in $hosts;
do
ssh -o "StrictHostKeyChecking=no"  -o "ConnectTimeout=3" root@$x 'echo $HOSTNAME'
done
}

foo