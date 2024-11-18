#!/bin/bash

INSTALL_DIR="/apps/modules/intel"

# Download intel oneapi hpc toolkit
wget https://registrationcenter-download.intel.com/akdlm/IRC_NAS/0884ef13-20f3-41d3-baa2-362fc31de8eb/intel-oneapi-hpc-toolkit-2025.0.0.825_offline.sh 

chmod +x intel-oneapi-hpc-toolkit-2025.0.0.825_offline.sh

sh ./intel-oneapi-hpc-toolkit-2025.0.0.825_offline.sh -a --components intel.oneapi.lin.dpcpp-cpp-compiler:intel.oneapi.lin.mkl.devel:intel.oneapi.lin.mpi.devel --silent --eula accept --install-dir $INSTALL_DIR 

