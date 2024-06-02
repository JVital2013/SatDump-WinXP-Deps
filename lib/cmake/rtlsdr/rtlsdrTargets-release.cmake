#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "rtlsdr::rtlsdr" for configuration "Release"
set_property(TARGET rtlsdr::rtlsdr APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(rtlsdr::rtlsdr PROPERTIES
  IMPORTED_IMPLIB_RELEASE "${_IMPORT_PREFIX}/lib/rtlsdr.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/rtlsdr.dll"
  )

list(APPEND _cmake_import_check_targets rtlsdr::rtlsdr )
list(APPEND _cmake_import_check_files_for_rtlsdr::rtlsdr "${_IMPORT_PREFIX}/lib/rtlsdr.lib" "${_IMPORT_PREFIX}/bin/rtlsdr.dll" )

# Import target "rtlsdr::rtlsdr_static" for configuration "Release"
set_property(TARGET rtlsdr::rtlsdr_static APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(rtlsdr::rtlsdr_static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C;RC"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/rtlsdr_static.lib"
  )

list(APPEND _cmake_import_check_targets rtlsdr::rtlsdr_static )
list(APPEND _cmake_import_check_files_for_rtlsdr::rtlsdr_static "${_IMPORT_PREFIX}/lib/rtlsdr_static.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
