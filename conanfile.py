#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os

class MongoCDriverConan(ConanFile):
    name = "mongo-c-driver"
    version = "1.9.4"
    url = "http://github.com/bincrafters/conan-mongo-c-driver"
    description = "A high-performance MongoDB driver for C "
    license = "https://github.com/mongodb/mongo-c-driver/blob/{0}/COPYING".format(version)
    settings = "os", "compiler", "arch", "build_type"
    requires = 'zlib/[~=1.2]@conan/stable'
    exports_sources = ["Find*.cmake", "header_path.patch", "CMakeLists.txt"]
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"
    generators = "cmake"

    def configure(self):
        # Because this is pure C
        del self.settings.compiler.libcxx

    def requirements(self):
        if not tools.os_info.is_macos and not tools.os_info.is_windows:
            self.requires.add("OpenSSL/1.0.2o@conan/stable")

    def source(self):
        tools.get("https://github.com/mongodb/mongo-c-driver/releases/download/{0}/mongo-c-driver-{0}.tar.gz".format(self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)
        tools.patch(base_path=self.source_subfolder, patch_file="header_path.patch")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["ENABLE_STATIC"] = "OFF" # static not supported yet... waiting for a PR
        cmake.definitions["ENABLE_TESTS"] = False
        cmake.definitions["ENABLE_EXAMPLES"] = False
        cmake.definitions["ENABLE_AUTOMATIC_INIT_AND_CLEANUP"] = False
        cmake.definitions["ENABLE_BSON"] = "ON"

        if self.settings.os != 'Windows':
            cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = True

        cmake.configure(build_folder=self.build_subfolder)
        cmake.build()
        cmake.install()

    def package(self):
        self.copy(pattern="COPYING*", src="sources")
        self.copy("Find*.cmake", ".", ".")
        # cmake installs all the files

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

        if tools.os_info.is_macos:
            self.cpp_info.exelinkflags = ['-framework CoreFoundation', '-framework Security']
            self.cpp_info.sharedlinkflags = self.cpp_info.exelinkflags

        if tools.os_info.is_linux:
            self.cpp_info.libs.extend(["rt", "ssl", "crypto", "dl", "pthread"])
