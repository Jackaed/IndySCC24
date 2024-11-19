export BUILD_PATH=/apps/modules
export OPENMPI=$BUILD_PATH/openmpi-5.0.5/bin
#export PATH=$OPENMPI:$PATH
#export TOOL_CHAIN=intel-chain
#export TOOL_CHAIN=open-chain

# Intel
#export CC=icx
#export CXX=icpx
#export FC=ifx
#export F77=ifx
#export F90=ifx
#export MPIFC="mpiifort -fc=ifx"
#export MPIF77="mpiifort -fc=ifx"
#export MPIF90="mpiifort -fc=ifx"
#export MPICC="mpiicc -cc=icx"
#export MPICXX="mpiicpc -cxx=icpx"

# Open
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

export ZLIB_ROOT=$BUILD_PATH/zlib-1.3.1
export HDF5_ROOT=$BUILD_PATH/hdf5-1.14.5
export NETCDFF_ROOT=$BUILD_PATH/netcdf-fortran-4.6.1
export NETCDF_ROOT=$BUILD_PATH/netcdf-c-4.9.2
export ECCODES_ROOT=$BUILD_PATH/eccodes-2.38.3
export XML2_ROOT=$BUILD_PATH/libxml2-2.13.4
export FYAML_ROOT=$BUILD_PATH/libfyaml-0.9
export MPI_ROOT=$BUILD_PATH/openmpi-5.0.5
export OPENBLAS_ROOT=$BUILD_PATH/openblas-0.3.28
# export GCC_ROOT=/usr/lib64
