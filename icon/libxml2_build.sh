#!/bin/bash
wget https://download.gnome.org/sources/libxml2/2.13/libxml2-2.13.4.tar.xz
tar -xJf libxml2-2.13.4.tar.xz
cd libxml2-2.13.4
mkdir build
CC=$CC FC=$FC CXX=$CXX CFLAGS="-O3" ./configure --prefix=$(pwd)/build --with-zlib=$ZLIB_ROOT
make -j
make install
cd ..
rm libxml2-2.13.4.tar.xz
