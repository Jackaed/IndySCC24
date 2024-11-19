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
wget https://github.com/Unidata/netcdf-fortran/archive/refs/tags/v4.6.1.tar.gz
tar -xzf v4.6.1.tar.gz
cd netcdf-fortran-4.6.1/
mkdir build
CPPFLAGS="-DgFortran -I${NETCDF_ROOT}/include -I${HDF5_ROOT}/include -I${ZLIB_ROOT}/include" \
	LDFLAGS="-L${NETCDF_ROOT}/lib -L${HDF5_ROOT}/lib -L${ZLIB_ROOT}/lib" \
	LD_LIBRARY_PATH=${NETCDF_ROOT}/lib:${HDF5_ROOT}/lib:${ZLIB_ROOT}/lib \
	LIBS="-lnetcdf -lhdf5_hl -lhdf5 -lz -lcurl -lm -lcurl" \
	./configure --prefix=$BUILD_PATH/netcdf-fortran-4.6.1
make -j
make -j install
cd ..
rm v4.6.1.tar.gz
