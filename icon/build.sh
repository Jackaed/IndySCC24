#!/bin/bash

source envvar.sh

# Install Intel Toolkit
./intel_build.sh

# Install zlib
./zlib_build.sh

# Install hdf5
./hdf5_build.sh

# Install netcdf-c
./netcdf-c_build.sh

# Install netcdf-f
./netcdf-f_build.sh

# Install eccodes
./eccodes_build.sh

# Install libxml2
./libxml2_build.sh

# Install libfyaml
libfyaml_build.sh
