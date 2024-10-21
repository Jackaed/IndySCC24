#!/bin/bash
wget https://github.com/madler/zlib/releases/download/v1.3.1/zlib-1.3.1.tar.gz
tar -xzf zlib-1.3.1.tar.gz
cd zlib-1.3.1/
./configure --static --prefix=$(pwd)/build
make
make install
cd ..
rm zlib-1.3.1.tar.gz
