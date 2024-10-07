# SatDump Windown XP Dependencies

These are 32-Bit Windows XP dependencies for SatDump. No support will be given for this repo. A Selection of build commands follow.

### RTLSDR

cmake .. -G "Visual Studio 17 2022" -A Win32 -T v141_xp -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DCMAKE_FIND_ROOT_PATH="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DLIBUSB_INCLUDE_DIRS="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows/include/libusb-1.0" -DLIBUSB_LIBRARIES="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows/lib/libusb-1.0.lib" -DTHREADS_PTHREADS_INCLUDE_DIR="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows/include" -DTHREADS_PTHREADS_LIBRARY="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows/lib/pthreadVC2.lib"

### HackRF

cmake .. -G "Visual Studio 17 2022" -A Win32 -T v141_xp -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DCMAKE_FIND_ROOT_PATH="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DLIBUSB_INCLUDE_DIR="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows/include/libusb-1.0" -DLIBUSB_LIBRARIES="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows/lib/libusb-1.0.lib" -DTHREADS_PTHREADS_INCLUDE_DIR="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows/include" -DTHREADS_PTHREADS_WIN32_LIBRARY="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows/lib/pthreadVC2.lib" -DFFTW_LIBRARIES="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows/lib/fftw3f.lib"

### Airspy/AirSpy HF

cmake .. -G "Visual Studio 17 2022" -A Win32 -T v141_xp -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DCMAKE_FIND_ROOT_PATH="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DLIBUSB_INCLUDE_DIR="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows/include/libusb-1.0" -DLIBUSB_LIBRARIES="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows/lib/libusb-1.0.lib" -DTHREADS_PTHREADS_INCLUDE_DIR="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows/include"

### BladeRF

cmake .. -G "Visual Studio 17 2022" -A Win32 -T v141_xp -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DCMAKE_FIND_ROOT_PATH="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DTEST_LIBBLADERF=OFF

### HDF5
cmake .. -G "Visual Studio 17 2022" -A Win32 -T v141_xp -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX="C:/Users/jvita/Programs/SatDump/vcpkg/installed/x64-windows" -DCMAKE_FIND_ROOT_PATH="C:/Users/jvita/Programs/SatDump/vcpkg/installed/x64-windows" -DBUILD_TESTING=OFF -DHDF5_BUILD_TOOLS=OFF -DHDF5_TEST_PLUGIN=OFF -DHDF5_BUILD_EXAMPLES=OFF

### MBedTLS

git clone https://github.com/Mbed-TLS/mbedtls -b v3.4.1
cmake .. -G "Visual Studio 17 2022" -A Win32 -T v141_xp -DCMAKE_INSTALL_PREFIX="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DCMAKE_FIND_ROOT_PATH="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DENABLE_PROGRAMS=OFF -DENABLE_TESTING=OFF

### NNG

git clone https://github.com/JVital2013/nng-xp
cmake .. -G "Visual Studio 17 2022" -A Win32 -T v141_xp -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DCMAKE_FIND_ROOT_PATH="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DNNG_ENABLE_TLS=ON -DNNG_TOOLS=OFF -DNNG_TESTS=OFF -DNNG_ENABLE_NNGCAT=OFF -DNNG_ENABLE_COMPAT=OFF

### Curl

cmake .. -G "Visual Studio 17 2022" -A Win32 -T v141_xp -DCMAKE_INSTALL_PREFIX="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DCMAKE_FIND_ROOT_PATH="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DCURL_USE_MBEDTLS=ON -DCURL_TARGET_WINDOWS_VERSION=0x0501 -DCURL_DEFAULT_SSL_BACKEND=mbedtls -DHTTP_ONLY=ON

### Zstd

cmake ../build/cmake -G "Visual Studio 17 2022" -A Win32 -T v141_xp -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DCMAKE_FIND_ROOT_PATH="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DZSTD_BUILD_PROGRAMS=OFF -DZSTD_BUILD_CONTRIB=OFF -DBUILD_TESTING=OFF -DZSTD_BUILD_STATIC=OFF

### Zlib

cmake ../build/cmake -G "Visual Studio 17 2022" -A Win32 -T v141_xp -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DCMAKE_FIND_ROOT_PATH="C:/Users/Jamie/Documents/Programs/SatDump/vcpkg/installed/x64-windows" -DZLIB_BUILD_EXAMPLES=OFF 
