#!/bin/bash
wget https://github.com/Unidata/netcdf-c/archive/refs/tags/v4.9.2.tar.gz
tar -xzf v4.9.2.tar.gz
cd netcdf-c-4.9.2/
mkdir build
CC=$MPICC CXX=$MPICXX CPPFLAGS="-I${HDF5_ROOT}/include -I${ZLIB_ROOT}/include" LDFLAGS="-L${HDF5_ROOT}/lib -L${ZLIB_ROOT}/lib" ./configure --enable-parallel --prefix=$(pwd)/build 
make -j
make install
cd ..
rm v4.9.2.tar.gz
