export BUILD_PATH=/apps/modules
export TOOL_CHAIN=intel-chain
#export TOOL_CHAIN=open-chain
export CC=icx
export CXX=icpx
export FC=ifx
export F77=ifx
export F90=ifx
export MPIFC="mpiifort -fc=ifx"
export MPIF77="mpiifort -fc=ifx"
export MPIF90="mpiifort -fc=ifx"
export MPICC="mpiicc -cc=icx"
export MPICXX="mpiicpc -cxx=icpx"
export ZLIB_ROOT=$BUILD_PATH/$TOOL_CHAIN/zlib-1.3.1
export HDF5_ROOT=$BUILD_PATH/$TOOL_CHAIN/hdf5-1.14.5
export NETCDFF_ROOT=$BUILD_PATH/$TOOL_CHAIN/netcdf-fortran-4.6.1
export NETCDF_ROOT=$BUILD_PATH/$TOOL_CHAIN/netcdf-c-4.9.2
export ECCODES_ROOT=$BUILD_PATH/$TOOL_CHAIN/eccodes-2.38.3
export XML2_ROOT=$BUILD_PATH/$TOOL_CHAIN/libxml2-2.13.4
export FYAML_ROOT=$BUILD_PATH/$TOOL_CHAIN/libfyaml-0.9

