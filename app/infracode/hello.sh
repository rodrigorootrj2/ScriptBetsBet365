#!/bin/bash
hosts=$(cat ../env/hosts)

function foo(){
for x in $hosts;
do
echo $x
done
}

foo