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

wget https://github.com/OpenMathLib/OpenBLAS/releases/download/v0.3.28/OpenBLAS-0.3.28.tar.gz
tar -zxf OpenBLAS-0.3.28.tar.gz
cd OpenBLAS-0.3.28
make -j USE_OPENMP=1
make -j PREFIX=$BUILD_PATH/openblas-0.3.28 install
cd ..
rm OpenBLAS-0.3.28.tar.gz 
