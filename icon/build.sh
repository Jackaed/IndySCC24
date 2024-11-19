#!/bin/bash

sudo dnf install make automake gcc gcc-c++ kernel-devel python3.9-devel m4 curl glibc-devel gfortran libcurl-devel -y
source envvar.sh

## Install Intel Toolkit
#./intel_build.sh
#source $BUILD_PATH/intel/setvars.sh

# module load openMPI
# module load openBLAS

## Install OpenMPI 
#./openmpi_build.sh

# Install OpenBLAS
#./openblas_build.sh

## Install zlib
#./zlib_build.sh

## Install hdf5
#./hdf5_build.sh

## Install netcdf-c
#./netcdf-c_build.sh

## Install netcdf-f
#./netcdf-f_build.sh

# Install eccodes
./eccodes_build.sh

# Install libxml2
./libxml2_build.sh

# Install libfyaml
./libfyaml_build.sh
