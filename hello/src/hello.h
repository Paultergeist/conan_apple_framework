#pragma once

#ifdef WIN32
  #define HELLO_EXPORT __declspec(dllexport)
#else
  #define HELLO_EXPORT __attribute__((visibility("default")))
#endif

#ifdef __cplusplus
extern "C" {
#endif
class HELLO_EXPORT Hello
{
	public:
		static void hello();
};
#ifdef __cplusplus
}
#endif
