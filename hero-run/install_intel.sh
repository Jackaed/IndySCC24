#!/bin/bash

INSTALL_DIR="/opt/intel/oneapi"

# Download intel oneapi hpc toolkit
wget https://registrationcenter-download.intel.com/akdlm/IRC_NAS/0884ef13-20f3-41d3-baa2-362fc31de8eb/intel-oneapi-hpc-toolkit-2025.0.0.825_offline.sh 

chmod +x intel-oneapi-hpc-toolkit-2025.0.0.825_offline.sh

# sh ./intel-oneapi-hpc-toolkit-2025.0.0.825_offline.sh -a --silent --eula accept --install-dir $INSTALL_DIR
sh ./intel-oneapi-hpc-toolkit-2025.0.0.825_offline.sh --list-components 
# sh ./intel-oneapi-base-toolkit-2025.0.0.885_offline.sh -a --silent --eula accept

