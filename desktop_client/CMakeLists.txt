cmake_minimum_required(VERSION 3.10)
project(BelliDiel_ERP VERSION 1.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

include_directories(include third_party/sqlite)

file(GLOB_RECURSE FUENTES "src/*.cpp")
set(SQLITE_FUENTE "third_party/sqlite/sqlite3.c")

add_executable(BelliDielApp ${FUENTES} ${SQLITE_FUENTE})