#!/bin/bash
export CC=$OPENMPI/mpicc
export CXX=$OPENMPI/mpic++
export FC=$OPENMPI/mpifort
export F77=$OPENMPI/mpif77
export F90=$OPENMPI/mpif90
export MPIFC=$OPENMPI/mpifort
export MPIF77=$OPENMPI/mpif77
export MPIF90=$OPENMPI/mpif90
export MPICC=$OPENMPI/mpicc
export MPICXX=$OPENMPI/mpic++
wget https://github.com/pantoniou/libfyaml/releases/download/v0.9/libfyaml-0.9.tar.gz
tar -xzf libfyaml-0.9.tar.gz
cd libfyaml-0.9
mkdir build
CFLAGS="-O3" ./configure --prefix=$BUILD_PATH/libfyaml-0.9
make -j
make -j install
cd ..
rm libfyaml-0.9.tar.gz
