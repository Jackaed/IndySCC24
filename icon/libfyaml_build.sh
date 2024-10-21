#!/bin/bash
wget https://github.com/pantoniou/libfyaml/releases/download/v0.9/libfyaml-0.9.tar.gz
tar -xzf libfyaml-0.9.tar.gz
cd libfyaml-0.9
mkdir build
CC=$CC CXX=$CXX CFLAGS="-O3" ./configure --prefix=$(pwd)/build
make -j
make install
cd ..
rm libfyaml-0.9.tar.gz
