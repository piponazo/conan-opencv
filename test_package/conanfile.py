from conans import ConanFile, CMake
from conans.errors import ConanException
import os

class OpenCVTestConan(ConanFile):

    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def imports(self):
        self.copy('*.dll', src='x64/vc12/bin/', dst=os.sep.join(['.', 'bin', '%s' % self.settings.build_type]))
        self.copy('*.dylib', src='lib', dst='lib')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.conanfile_directory, build_dir="./")
        cmake.build()

    def test(self):
        self.run(os.sep.join(['.', 'bin', 'example']))
