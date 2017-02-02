from conans import ConanFile, CMake
from conans.errors import ConanException
import os

username = os.getenv("CONAN_USERNAME", "piponazo")
channel = os.getenv("CONAN_CHANNEL", "testing")

class OpenCVTestConan(ConanFile):

    settings = "os", "compiler", "build_type", "arch"
    requires = "OpenCV/3.1.0-0@%s/%s" % (username, channel)
    generators = "cmake"

    def imports(self):
        if self.settings.os == 'Windows':
            self.copy('*.dll', src='x64/vc12/bin/', dst=os.sep.join(['.', 'bin', '%s' % self.settings.build_type]))
        if self.settings.os == 'Macos':
            self.copy('*.dylib', src='lib', dst='lib')

    def build(self):
        cmake = CMake(self.settings)
        cmake_options = ['CMAKE_BUILD_TYPE=%s' % self.settings.build_type]

        options = '-D' + ' -D'.join(cmake_options)

        self.run('cmake "%s" %s %s' % (self.conanfile_directory, cmake.command_line, options))
        self.run('cmake --build . %s' % cmake.build_config)

    def test(self):
        if self.settings.os == 'Windows':
            self.run(os.sep.join(['.', 'bin', '%s' % self.settings.build_type, 'test']))
        else:
            self.run(os.sep.join(['.', 'bin', 'test']))
