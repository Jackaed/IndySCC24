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
wget https://github.com/Unidata/netcdf-c/archive/refs/tags/v4.9.2.tar.gz
tar -xzf v4.9.2.tar.gz
cd netcdf-c-4.9.2/
mkdir build
CPPFLAGS="-I${HDF5_ROOT}/include -I${ZLIB_ROOT}/include" LDFLAGS="-L${HDF5_ROOT}/lib -L${ZLIB_ROOT}/lib" ./configure --disable-libxml2 --disable-byterange --prefix=$BUILD_PATH/netcdf-c-4.9.2
make -j
make -j install
cd ..
rm v4.9.2.tar.gz

