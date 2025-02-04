from conan import ConanFile
from conan.tools.cmake.layout import cmake_layout;

class UnoRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    options = {"shared" : [True, False]}
    default_options = {"shared" : True}

    # taking latest folly avaialble
    # not specifying versions of boost and fmt as folly will force it's own versions
    def requirements(self):
        self.requires("folly/[]")
        self.requires("boost/[]")
        self.requires("fmt/[]")
        self.requires("gtest/[^1]")

    def layout(self):
        cmake_layout(self)
