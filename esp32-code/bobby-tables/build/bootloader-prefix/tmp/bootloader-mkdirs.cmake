# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "C:/Users/Harry/esp/esp-idf/components/bootloader/subproject"
  "C:/Users/Harry/Desktop/Uni/COMP6733/comp6733-bobby-tables/esp32-code/bobby-tables/build/bootloader"
  "C:/Users/Harry/Desktop/Uni/COMP6733/comp6733-bobby-tables/esp32-code/bobby-tables/build/bootloader-prefix"
  "C:/Users/Harry/Desktop/Uni/COMP6733/comp6733-bobby-tables/esp32-code/bobby-tables/build/bootloader-prefix/tmp"
  "C:/Users/Harry/Desktop/Uni/COMP6733/comp6733-bobby-tables/esp32-code/bobby-tables/build/bootloader-prefix/src/bootloader-stamp"
  "C:/Users/Harry/Desktop/Uni/COMP6733/comp6733-bobby-tables/esp32-code/bobby-tables/build/bootloader-prefix/src"
  "C:/Users/Harry/Desktop/Uni/COMP6733/comp6733-bobby-tables/esp32-code/bobby-tables/build/bootloader-prefix/src/bootloader-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/Users/Harry/Desktop/Uni/COMP6733/comp6733-bobby-tables/esp32-code/bobby-tables/build/bootloader-prefix/src/bootloader-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "C:/Users/Harry/Desktop/Uni/COMP6733/comp6733-bobby-tables/esp32-code/bobby-tables/build/bootloader-prefix/src/bootloader-stamp${cfgdir}") # cfgdir has leading slash
endif()
