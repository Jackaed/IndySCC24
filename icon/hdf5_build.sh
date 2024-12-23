#!/bin/bash
echo $BUILD_PATH
ls $BUILD_PATH
wget https://github.com/HDFGroup/hdf5/releases/download/hdf5_1.14.5/hdf5-1.14.5.tar.gz
tar -xzf hdf5-1.14.5.tar.gz
cd hdf5-1.14.5
CC=$MPICC FC=$MPIFC CXX=$MPICXX F90=$MPIF90 F77=$MPIF77 CFLAGS="-O3" ./configure --prefix=$BUILD_PATH/hdf5-1.14.5 --with-zlib=$ZLIB_ROOT --enable-build-mode=production --enable-fortran --enable-parallel
make -j
make -j install
cd ..
rm hdf5-1.14.5.tar.gz
