#!/bin/bash
wget https://confluence.ecmwf.int/download/attachments/45757960/eccodes-2.38.3-Source.tar.gz
tar -xzf eccodes-2.38.3-Source.tar.gz
cd eccodes-2.38.3-Source/
mkdir build
mkdir install
BUILD=$(pwd)/build
cd install
cmake -DENABLE_AEC=OFF -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DCMAKE_INSTALL_PREFIX=${BUILD} ../../eccodes-2.38.3-Source
make
make install
cd ../../
rm eccodes-2.38.3-Source.tar.gz

