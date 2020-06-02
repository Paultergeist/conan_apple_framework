cmake_minimum_required(VERSION 3.16)
project(MyHello CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# set @rpaths for libraries to link against
SET(CMAKE_SKIP_RPATH FALSE)
#SET(CMAKE_SKIP_BUILD_RPATH  FALSE)
#SET(CMAKE_INSTALL_RPATH "@rpath/")
#SET(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)


add_library(hello SHARED hello.cpp hello.h)
set_target_properties(hello PROPERTIES
  FRAMEWORK TRUE
  FRAMEWORK_VERSION A
  MACOSX_FRAMEWORK_IDENTIFIER com.cmake.hello
  MACOSX_FRAMEWORK_INFO_PLIST src/Info.plist
  # "current version" in semantic format in Mach-O binary file
  VERSION 1.6.0
  # "compatibility version" in semantic format in Mach-O binary file
  SOVERSION 1.6.0
  PUBLIC_HEADER hello.h
  INSTALL_NAME_DIR "@rpath"
  MACOSX_RPATH TRUE
)

#add_custom_command(TARGET hello
#    POST_BUILD COMMAND 
#    ${CMAKE_INSTALL_NAME_TOOL} -id "@rpath/hello.framework/hello" $<TARGET_FILE:hello>)

install(TARGETS hello
	DESTINATION ".")
