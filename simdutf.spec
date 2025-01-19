%define major 14
%define libname %mklibname simdutf
%define devname %mklibname simdutf -d

Name:		simdutf
Version:	6.0.3
Release:	1
Source0:	https://github.com/simdutf/simdutf/archive/refs/tags/v%{version}.tar.gz
Summary:	Unicode (UTF8/UTF16/UTF32) and Base64 library using SIMD instructions
URL:		https://github.com/simdutf/simdutf
License:	Apache-2.0
Group:		System/Libraries
BuildRequires:	cmake
BuildSystem:	cmake

%description
Unicode (UTF8/UTF16/UTF32) and Base64 library using SIMD instructions

%package -n %{libname}
Summary:	Unicode (UTF8/UTF16/UTF32) and Base64 library using SIMD instructions
Group:		System/Libraries

%description -n %{libname}
Unicode (UTF8/UTF16/UTF32) and Base64 library using SIMD instructions

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Unicode (UTF8/UTF16/UTF32) and Base64 library using SIMD instructions

%prep
%autosetup -p1

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
