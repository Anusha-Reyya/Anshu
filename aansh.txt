#!/bin/bash
set -e 
 
mkdir anusha
cd anusha
   
for i in {1..5}; 
do 
   mkdir folder$i;
   cd folder$i;
   touch file$i;
   cd ..;
done
