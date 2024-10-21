#!/bin/bash
wget https://github.com/Unidata/netcdf-fortran/archive/refs/tags/v4.6.1.tar.gz
tar -xzf v4.6.1.tar.gz
cd netcdf-fortran-4.6.1/
mkdir build
CC=$MPICC FC=$MPIFC CXX=$MPICXX F90=$MPIF90 F77=$MPIF77 \
	CPPFLAGS="-DgFortran -I${NETCDF_ROOT}/include -I${HDF5_ROOT}/include -I${ZLIB_ROOT}/include" \
	LDFLAGS="-L${NETCDF_ROOT}/lib -L${HDF5_ROOT}/lib -L${ZLIB_ROOT}/lib" \
	LD_LIBRARY_PATH=${NETCDF_ROOT}/lib:${HDF5_ROOT}/lib:${ZLIB_ROOT}/lib \
	LIBS="-lhdf5_hl -lhdf5 -lz -lcurl" \
	./configure --disable-shared --prefix=$(pwd)/build 
make -j
make install
cd ..
rm v4.6.1.tar.gz
