#!/bin/bash
for i in {5..8}
do
    useradd -m -s /bin/bash "user$i"
    echo "user$i:Test@1325_"|chpasswd
done
