conan remove -f hello_framework
conan remove -f use_hello_framework

conan create hello test/test -pr profiles/test_ios
conan create use_hello test/test -pr profiles/test_ios

