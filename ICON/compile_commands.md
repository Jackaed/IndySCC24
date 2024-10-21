# Compiling ICON

## Download ICON:


## Download dependencies

export CC=/apps/modules/openmpi/bin/mpicc
export FC=/apps/modules/openmpi/bin/mpifc

## HDF5

download hdf5, decompress
./configure --enable-parallel --enable-fortran --prefix=/apps/modules/hdf5-1.14.5
make -j check install

## netcdf-c

CPPFLAGS="-I/apps/modules/hdf5-1.14.5/include -I/apps/modules/zlib/include -I/apps/modules/pnetcdf-1.13.0/include" MPI_ROOT=/apps/modules/openmpi/ LDFLAGS="-L/apps/modules/hdf5-1.14.5/lib -L/apps/modules/zlib/lib -L//apps/modules/pnetcdf-1.13.0/lib" ./configure --disable-shared --enable-parallel-tests --enable-fortran --enable-pnetcdf --prefix=/apps/modules/netcdf-c-4.9.2

## netcdf-fortran

H5DIR=/apps/modules/hdf5-1.14.5 NCDIR=/apps/modules/netcdf-c-4.9.2 FC=/apps/modules/openmpi/bin/mpif90 F77=/apps/modules/openmpi/bin/mpif77 CC=/apps/modules/openmpi/bin/mpicc CPPFLAGS="-I${NCDIR}/include -I${H5DIR}/include -I/apps/modules/zlib/include -I/usr/include" LDFLAGS="-L${NCDIR}/lib -L${H5DIR}/lib -L/apps/modules/zlib/lib -L/usr/lib64" LD_LIBRARY_PATH=${NCDIR}/lib:${H5DIR}/lib:/apps/modules/zlib/lib:/usr/lib64 LIBS="-lnetcdf -lhdf5_hl -lhdf5 -lz -lcurl -lm -lzstd -lxml2 -lcurl" ./configure --disable-shared --enable-static --prefix=/apps/modules/netcdf-fortran-4.6.1
