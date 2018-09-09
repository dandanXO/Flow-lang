cmake_minimum_required(VERSION 3.10)
project(Flow_lang)

set(CMAKE_CXX_STANDARD 17)

find_package(LLVM REQUIRED CONFIG)

include_directories(.)

include_directories(${LLVM_INCLUDE_DIRS})
add_definitions(${LLVM_DEFINITIONS})

add_executable(flowc
        main.cxx
        scanner/scanner.cxx
        frontend/frontend.cxx
        ast/ast.cxx
        parser/parser.cxx
        )

target_link_libraries(flowc)
