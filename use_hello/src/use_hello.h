#pragma once

#ifdef WIN32
  #define USE_HELLO_EXPORT __declspec(dllexport)
#else
  #define USE_HELLO_EXPORT __attribute__((visibility("default")))
#endif

#ifdef __cplusplus
extern "C" {
#endif

USE_HELLO_EXPORT void use_hello();

#ifdef __cplusplus
}
#endif
