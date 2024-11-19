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
wget https://confluence.ecmwf.int/download/attachments/45757960/eccodes-2.38.3-Source.tar.gz
tar -xzf eccodes-2.38.3-Source.tar.gz
cd eccodes-2.38.3-Source/
mkdir build
mkdir install
cd install
cmake -DENABLE_AEC=OFF -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$BUILD_PATH/eccodes-2.38.3 ../../eccodes-2.38.3-Source
make -j
make -j install
cd ../../
rm eccodes-2.38.3-Source.tar.gz

