#!/bin/bash
wget https://registrationcenter-download.intel.com/akdlm/IRC_NAS/89a381f6-f85d-4dda-ae62-30d51470f53c/l_onemkl_p_2024.2.2.17_offline.sh
chmod +x l_onemkl_p_2024.2.2.17_offline.sh
./l_onemkl_p_2024.2.2.17_offline.sh -a --silent --cli --eula accept --install-dir $BUILD_PATH/intel
rm l_onemkl_p_2024.2.2.17_offline.sh

wget https://registrationcenter-download.intel.com/akdlm/IRC_NAS/d461a695-6481-426f-a22f-b5644cd1fa8b/l_HPCKit_p_2024.2.1.79_offline.sh
chmod +x l_HPCKit_p_2024.2.1.79_offline.sh
./l_HPCKit_p_2024.2.1.79_offline.sh -a --silent --cli --eula accept --install-dir $BUILD_PATH/intel
rm l_HPCKit_p_2024.2.1.79_offline.sh

source $BUILD_PATH/intel/oneapi/setvars.sh
