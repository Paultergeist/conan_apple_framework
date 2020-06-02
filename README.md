`hello` - simple framework

`use_hello` - another simple framework that depends on `hello`

`test_macos.sh`, `test_ios.sh`, `test_tvos.sh` - scripts to build `hello` and then `use_hello` for macOS, iOS, and tvOS correspondingly

`profiles` - profiles for easy building for those platforms

Building for macOS works fine

Building for iOS and tvOS fails with the error
```
CMake Error at ../conanbuildinfo.cmake:26 (message):
  Framework library hello not found in paths:
  /path/to/.conan/data/hello_framework/1.0.0/test/test/package/1ad6c19faab0c790fcbf49a0aefb3676ae597d05
Call Stack (most recent call first):
  ../conanbuildinfo.cmake:66 (conan_find_apple_frameworks)
  CMakeLists.txt:4 (include)
```

As a workaround,
 ```
 set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY NEVER)
```
before 
```
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
```
makes it work, but it should probably be done inside `conanbuildinfo.cmake`. Or maybe there is a better way to fix it.
