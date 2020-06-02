cmake_minimum_required(VERSION 3.16)
project(apple_app CXX OBJCXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

SET(CMAKE_SKIP_RPATH FALSE)

add_library(use_hello SHARED use_hello.mm use_hello.h)
target_link_libraries(use_hello ${CONAN_LIBS})
set_target_properties(use_hello PROPERTIES
  FRAMEWORK TRUE
  FRAMEWORK_VERSION A
  MACOSX_FRAMEWORK_IDENTIFIER com.cmake.use_hello
  MACOSX_FRAMEWORK_INFO_PLIST src/Info.plist
  # "current version" in semantic format in Mach-O binary file
  VERSION 1.6.0
  # "compatibility version" in semantic format in Mach-O binary file
  SOVERSION 1.6.0
  PUBLIC_HEADER use_hello.h
  INSTALL_NAME_DIR "@rpath"
  MACOSX_RPATH TRUE
)

install(TARGETS use_hello
	DESTINATION ".")

