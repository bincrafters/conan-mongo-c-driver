[![Download](https://api.bintray.com/packages/bincraters/public-conan/mongo-c-driver%3Abincraters/images/download.svg) ](https://bintray.com/bincraters/public-conan/mongo-c-driver%3Abincraters/_latestVersion)
[![Build Status](https://travis-ci.org/bincraters/conan-mongo-c-driver.svg?branch=stable%2F1.9.4)](https://travis-ci.org/bincraters/conan-mongo-c-driver)
[![Build status](https://ci.appveyor.com/api/projects/status/github/bincraters/conan-mongo-c-driver?branch=stable%2F1.9.4&svg=true)](https://ci.appveyor.com/project/bincraters/conan-mongo-c-driver)

[Conan.io](https://conan.io) package recipe for *mongo-c-driver*.

A high-performance MongoDB driver for C 

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/bincraters/public-conan/mongo-c-driver%3Abincraters).

## For Users: Use this package

### Basic setup

    $ conan install mongo-c-driver/1.9.4@bincraters/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    mongo-c-driver/1.9.4@bincraters/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincraters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create bincraters/stable


### Available Options
| Option        | Default | Possible Values  |
| ------------- |:----------------- |:------------:|
| shared      | False |  [True, False] |

## Add Remote

    $ conan remote add bincraters "https://api.bintray.com/conan/bincraters/public-conan"

## Upload

    $ conan upload mongo-c-driver/1.9.4@bincraters/stable --all -r bincraters


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package mongo-c-driver.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](git@github.com:bincrafters/conan-mongo-c-driver.git/blob/stable/1.9.4/LICENSE.md)
