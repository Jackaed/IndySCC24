#!/bin/bash

source envvar.sh
mkdir $BUILD_PATH/$TOOL_CHAIN
sudo dnf install m4 curl -y

# Install Intel Toolkit
#./intel_build.sh
source $BUILD_PATH/intel/setvars.sh

# Install zlib
#./zlib_build.sh

# Install hdf5
#./hdf5_build.sh

# Install netcdf-c
#./netcdf-c_build.sh

# Install netcdf-f
./netcdf-f_build.sh

# Install eccodes
#./eccodes_build.sh

# Install libxml2
#./libxml2_build.sh

# Install libfyaml
#./libfyaml_build.sh
