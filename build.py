from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(build_types=['Release'],
                                 archs=['x86_64']
                                )
    builder.add_common_builds()
    builder.run()
