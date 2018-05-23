from conans import ConanFile, CMake
from conans.errors import ConanException
import os

class OpenCVTestConan(ConanFile):

    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def imports(self):
        self.copy('*.dll', src='x64/vc%s/bin/' % self.settings.compiler.version, dst='bin')
        self.copy('*.dylib', src='lib', dst='bin')

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        os.chdir('bin')
        self.run(os.sep.join(['.', 'example']))
