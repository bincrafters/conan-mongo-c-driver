#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os

class MongoCDriverConan(ConanFile):
    name = "mongo-c-driver"
    version = "1.11.0"
    url = "http://github.com/bincrafters/conan-mongo-c-driver"
    homepage = "https://github.com/mongodb/mongo-c-driver"
    description = "A high-performance MongoDB driver for C "
    license = "https://github.com/mongodb/mongo-c-driver/blob/{0}/COPYING".format(version)
    settings = "os", "compiler", "arch", "build_type"
    requires = 'zlib/1.2.11@conan/stable'
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=True", "fPIC=True"
    exports_sources = ["Find*.cmake", "header_path.patch", "CMakeLists.txt"]
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"
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
        os.rename(extracted_dir, self._source_subfolder)
        tools.patch(base_path=self._source_subfolder, patch_file="header_path.patch")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["ENABLE_TESTS"] = False
        cmake.definitions["ENABLE_EXAMPLES"] = False
        cmake.definitions["ENABLE_AUTOMATIC_INIT_AND_CLEANUP"] = False
        cmake.definitions["ENABLE_BSON"] = "ON"
        cmake.definitions["ENABLE_SASL"] = "OFF"
        cmake.definitions["ENABLE_STATIC"] = "OFF" if self.options.shared else "ON"

        cmake.configure(build_folder=self._build_subfolder)

        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="COPYING*", src="sources")
        self.copy("Find*.cmake", ".", ".")

        # cmake installs all the files
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ['mongoc-1.0', 'bson-1.0'] if self.options.shared else ['mongoc-static-1.0', 'bson-static-1.0']

        if tools.os_info.is_macos:
            self.cpp_info.exelinkflags = ['-framework CoreFoundation', '-framework Security']
            self.cpp_info.sharedlinkflags = self.cpp_info.exelinkflags

        if tools.os_info.is_linux:
            self.cpp_info.libs.extend(["rt", "pthread"])

        if not self.options.shared:
            if tools.os_info.is_linux or tools.os_info.is_macos:
                self.cpp_info.libs.append('resolv')

            if tools.os_info.is_windows:
                self.cpp_info.libs.extend(['ws2_32.lib', 'BCrypt.lib'])
