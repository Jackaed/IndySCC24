#!/bin/bash
wget https://confluence.ecmwf.int/download/attachments/45757960/eccodes-2.38.3-Source.tar.gz
tar -xzf eccodes-2.38.3-Source.tar.gz
cd eccodes-2.38.3-Source/
mkdir build
mkdir install
cd install
cmake -DENABLE_AEC=OFF -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$BUILD_PATH/$TOOL_CHAIN/eccodes-2.38.3 ../../eccodes-2.38.3-Source
make
make install
cd ../../
rm eccodes-2.38.3-Source.tar.gz

