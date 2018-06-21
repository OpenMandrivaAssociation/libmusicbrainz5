%define oname	libmusicbrainz
%define api	5
%define major	1
%define libname	%mklibname musicbrainz %{api} %{major}
%define devname	%mklibname -d musicbrainz %{api}

Summary:	A software library for accesing MusicBrainz servers
Name:		libmusicbrainz5
Version:	5.1.0
Release:	2
Group:		Sound
License:	LGPLv2+
Url:		http://musicbrainz.org/doc/libmusicbrainz
Source0:	https://github.com/metabrainz/libmusicbrainz/archive/release-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(neon)
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:	pkgconfig(libxml-2.0)
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
%setup -qn %{oname}-release-%{version}
%apply_patches

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if "%_lib" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	-G Ninja \
	.

%ninja

%install
%ninja_install

%files -n %{libname}
%{_libdir}/libmusicbrainz%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS.txt COPYING.txt NEWS.txt
%{_includedir}/musicbrainz%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmusicbrainz%{api}.pc

