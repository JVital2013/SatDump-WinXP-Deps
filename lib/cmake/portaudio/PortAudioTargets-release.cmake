#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "PortAudio::PortAudio" for configuration "Release"
set_property(TARGET PortAudio::PortAudio APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(PortAudio::PortAudio PROPERTIES
  IMPORTED_IMPLIB_RELEASE "${_IMPORT_PREFIX}/lib/portaudio.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/portaudio.dll"
  )

list(APPEND _cmake_import_check_targets PortAudio::PortAudio )
list(APPEND _cmake_import_check_files_for_PortAudio::PortAudio "${_IMPORT_PREFIX}/lib/portaudio.lib" "${_IMPORT_PREFIX}/bin/portaudio.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
