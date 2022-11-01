cmake_minimum_required(VERSION 3.12)

project(asr LANGUAGES C)

enable_testing()

add_library(asr SHARED src/asr.c)
add_library(asrStatic STATIC src/asr.c)

# Thanks to https://www.foonathan.net/2018/10/cmake-warnings/ for explaining
# how to the error flags properly.
target_compile_options(asr PRIVATE
    $<$<OR:$<C_COMPILER_ID:Clang>,$<C_COMPILER_ID:AppleClang>,$<C_COMPILER_ID:GNU>>:-Wall -Werror>
    $<$<C_COMPILER_ID:MSVC>:/W4 /WX>)
target_compile_options(asrStatic PRIVATE
    $<$<OR:$<C_COMPILER_ID:Clang>,$<C_COMPILER_ID:AppleClang>,$<C_COMPILER_ID:GNU>>:-Wall -Werror>
    $<$<C_COMPILER_ID:MSVC>:/W4 /WX>)

add_test(
    NAME asrHypothesisTests
    COMMAND python -m pytest ${CMAKE_CURRENT_LIST_DIR}/test/test_asr.py
    WORKING_DIRECTORY $<TARGET_FILE_DIR:asr>
)
