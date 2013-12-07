%define oname	libmusicbrainz
%define api	5
%define major	0
%define libname	%mklibname musicbrainz %{api} %{major}
%define devname	%mklibname -d musicbrainz %{api}

Summary:	A software library for accesing MusicBrainz servers
Name:		libmusicbrainz5
Version:	5.0.1
Release:	6
Group:		Sound
License:	LGPLv2+
Url:		http://musicbrainz.org/doc/libmusicbrainz
Source0:	https://github.com/downloads/metabrainz/libmusicbrainz/%{oname}-%{version}.tar.gz
Patch0:		cmake_include_dir.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(neon)
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:	pkgconfig(cppunit)

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package -n %{libname}
Summary:	A software library for accesing MusicBrainz servers
Group:		System/Libraries

%description -n %{libname}
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package -n %{devname}
Summary:	Headers for developing programs that will use libmusicbrainz
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use libmusicbrainz.

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if "%_lib" != "lib"
	-DLIB_SUFFIX=64 \
%endif

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libmusicbrainz%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS.txt COPYING.txt NEWS.txt
%{_includedir}/musicbrainz%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmusicbrainz%{api}.pc

