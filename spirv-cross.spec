Name:           spirv-cross
Version:        1.4.335.0
Release:        1%{?dist}
Summary:        SPIRV-Cross is a practical tool and library for performing reflection on SPIR-V and disassembling SPIR-V back to high-level languages.

License:        Apache-2.0
URL:            https://github.com/KhronosGroup/SPIRV-Cross
Source0:        https://github.com/KhronosGroup/SPIRV-Cross/archive/refs/tags/vulkan-sdk-%{version}.tar.gz

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++
BuildRequires:  make

%define debug_package %{nil}

%global _hardened_build 1

%description
SPIRV-Cross is a tool and library for parsing and converting SPIR-V to other shader languages.
It is commonly used in graphics development to convert SPIR-V bytecode into GLSL, HLSL, Metal Shading Language, and more.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the static libraries (PIC-enabled), headers, pkgconfig files, and CMake
modules needed to develop applications using SPIRV-Cross.

%prep
%setup -q -n SPIRV-Cross-vulkan-sdk-%{version}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DSPIRV_CROSS_STATIC=ON \
    -DSPIRV_CROSS_FORCE_PIC=ON \
    -DSPIRV_CROSS_ENABLE_TESTS=OFF \
    -DSPIRV_CROSS_CLI=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/spirv-cross

%files devel
%{_includedir}/spirv_cross/
%{_libdir}/libspirv-cross-*.a
%{_libdir}/pkgconfig/spirv-cross-*.pc
%{_datadir}/spirv_cross_*/cmake/

%changelog
* Wed Dec 24 2025 Your Name <your.email@example.com> - 1.4.335.0-1
- Static PIC build with separate modular .a libs (core, cpp, etc.) to match common distro packaging
- Explicit SPIRV_CROSS_STATIC=ON and CLI=ON; FORCE_PIC=ON for Fedora/PIE compatibility
- RelWithDebInfo for optimized build with symbols; tests off
- devel subpackage for libs/headers; base for CLI only

* Thu Oct 05 2023 Your Name <saypaul@redhat.com> - 1.4.304-1
- Initial package for SPIRV-Cross.
