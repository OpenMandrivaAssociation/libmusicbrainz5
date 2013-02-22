%define package_name libmusicbrainz

%define api 5
%define major 0
%define libname %mklibname musicbrainz %api %{major}
%define develname %mklibname -d musicbrainz %api

Name:		libmusicbrainz5
Version:	5.0.1
Release:	3
Summary:	A software library for accesing MusicBrainz servers
Source0:	https://github.com/downloads/metabrainz/libmusicbrainz/%{package_name}-%{version}.tar.gz
Patch0:		cmake_include_dir.patch
URL:		http://musicbrainz.org/doc/libmusicbrainz
Group:		Sound
License:	LGPLv2+
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

%package -n %{develname}
Summary:	Headers for developing programs that will use libmusicbrainz
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use libmusicbrainz.

%prep
%setup -q -n %{package_name}-%{version}
%apply_patches

%build
cmake . -DCMAKE_INSTALL_PREFIX=%_prefix -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if "%_lib" != "lib"
    -DLIB_SUFFIX=64 \
%endif

%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS.txt COPYING.txt NEWS.txt
%{_libdir}/libmusicbrainz%{api}.so.%{major}*

%files -n %{develname}
%{_includedir}/musicbrainz%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmusicbrainz%{api}.pc


%changelog
* Wed May 16 2012 Götz Waschk <waschk@mandriva.org> 5.0.1-1
+ Revision: 799259
- new version
- drop patch 1

* Wed May 16 2012 Götz Waschk <waschk@mandriva.org> 5.0.0-1
+ Revision: 799142
- new major
- new API
- new version
- fork for new version
- fix a build error
- new version
- fix source URL
- new major
- update build deps
- new version
- fix build
- new version with a new API
- new version
- drop patch
- fix for gcc 4.4
- new version
- drop patch
- fix build with gcc 4.3
- fix cmake call to have the right libdir on x86_64
- import libmusicbrainz3

  + Alexander Khrukin <akhrukin@mandriva.org>
    - version update 4.0.1
    - pkgconfig(libname) instead of libname-devel

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild
    - rebuilt for 2010.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

