#!/bin/bash
wget -N https://download.open-mpi.org/release/open-mpi/v5.0/openmpi-5.0.5.tar.gz
tar -zxf openmpi-5.0.5.tar.gz 
cd openmpi-5.0.5
./configure --prefix=$BUILD_PATH/openmpi-5.0.5
make -j
make -j install
cd ..
rm openmpi-5.0.5.tar.gz 

