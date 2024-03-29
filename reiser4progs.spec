%define enable_debug 1

Name: reiser4progs
Version: 1.2.2
Release: 1
Summary: Utilities for reiser4 filesystems
License: GPL
Group: System Environment/Base
URL: http://www.namesys.com/
Source: reiser4progs-%{version}.tar.gz
BuildRequires: libaal-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Utilities for manipulating reiser4 filesystems.

%package devel
Summary: Development libraries and headers for developing reiser4 tools.
Group: Development/Libraries

%description devel
Development libraries and headers for developing reiser4 tools.

%prep
%setup -q

%build
%configure \
%if %{enable_debug}
        --enable-debug \
%else
        --disable-debug \
%endif
        --enable-libminimal \
        --disable-plugins-check \
        --disable-fnv1-hash \
        --disable-rupasov-hash \
        --disable-tea-hash \
        --disable-deg-hash
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING CREDITS INSTALL NEWS README THANKS TODO
%{_libdir}/libreiser4-1.0.so.*
%{_libdir}/libreiser4-minimal-1.0.so.*
%{_libdir}/librepair-1.0.so.*
%{_sbindir}/debugfs.reiser4
%{_sbindir}/fsck.reiser4
%{_sbindir}/make_reiser4
%{_sbindir}/measurefs.reiser4
%{_sbindir}/mkfs.reiser4
%{_mandir}/man8/*.gz

%files devel
%dir %{_includedir}/reiser4
%{_includedir}/reiser4/*.h
%{_includedir}/repair/*.h
%{_datadir}/aclocal/libreiser4.m4
%{_libdir}/libreiser4.*a
%{_libdir}/libreiser4-minimal.*a
%{_libdir}/librepair.*a

%changelog
* Sat Aug 14 2004 neeo <neeo@irc.pl>
- Small update for 1.0
* Fri Aug 29 2003 Yuey V Umanets <umka@namesys.com>
- Some cleanups and improvements inf this spec file
* Wed Aug 27 2003 David T Hollis <dhollis@davehollis.com>
- RPM package created
