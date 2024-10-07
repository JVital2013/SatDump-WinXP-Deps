# - Config file for the SZIP package
# It defines the following variables
#  SZIP_INCLUDE_DIRS - include directories for szip
#  SZIP_LIBRARIES    - libraries to link against
#  SZIP_VERSION      - szip version

# Our library dependencies (contains definitions for IMPORTED targets)
if(NOT TARGET szip AND NOT SZIP_BINARY_DIR)
  include("${CMAKE_CURRENT_LIST_DIR}/SZIPTargets.cmake")
endif()
get_property(SZIP_INCLUDE_DIRS TARGET szip PROPERTY INTERFACE_INCLUDE_DIRECTORIES)

# These are IMPORTED targets created by SZIPTargets.cmake
set(SZIP_LIBRARIES szip)
set(SZIP_VERSION "2.1.1")
set(SZIP_FOUND TRUE)
