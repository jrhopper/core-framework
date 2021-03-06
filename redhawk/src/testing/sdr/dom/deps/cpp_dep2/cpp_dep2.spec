#
# This file is protected by Copyright. Please refer to the COPYRIGHT file
# distributed with this source distribution.
#
# This file is part of REDHAWK core.
#
# REDHAWK core is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# REDHAWK core is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.
#
# By default, the RPM will install to the standard REDHAWK SDR root location (/var/redhawk/sdr)
%{!?_sdrroot: %define _sdrroot /var/redhawk/sdr}
%define _prefix %{_sdrroot}/dom/deps/cpp_dep2

# Point install paths to locations within our target SDR root
%define _libdir        %{_prefix}/cpp/lib
%define _sysconfdir    %{_prefix}/etc
%define _localstatedir %{_prefix}/var
%define _mandir        %{_prefix}/man
%define _infodir       %{_prefix}/info

Name:           cpp_dep2
Version:        1.0.0
Release:        1%{?dist}
Summary:        Shared package %{name}

Group:          REDHAWK/Shared Packages
License:        None
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  redhawk-devel >= 2.0
BuildRequires:  autoconf automake libtool



%description
Shared package %{name}

%package devel
Summary:        Shared package %{name}
Group:          REDHAWK/Shared Packages
Requires:       %{name} = %{version}-%{release}

%description devel
Libraries and header files for shared package %{name}

%prep
%setup -q


%build
# Implementation cpp
pushd cpp
./reconf
%configure --with-sdr=%{_sdrroot}
make %{?_smp_mflags}
popd


%install
rm -rf $RPM_BUILD_ROOT
# Implementation cpp
pushd cpp
make install DESTDIR=$RPM_BUILD_ROOT
popd


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,redhawk,redhawk,-)
%dir %{_sdrroot}/dom/deps/cpp_dep2
%{_prefix}/cpp_dep2.spd.xml
%{_prefix}/cpp
%exclude %{_libdir}/libcpp_dep2.la
%exclude %{_libdir}/libcpp_dep2.so
%exclude %{_libdir}/pkgconfig

%files devel
%defattr(-,redhawk,redhawk,-)
%{_libdir}/libcpp_dep2.la
%{_libdir}/libcpp_dep2.so
%{_libdir}/pkgconfig
%{_prefix}/include

