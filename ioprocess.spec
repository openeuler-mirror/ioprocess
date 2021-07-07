Name:		ioprocess
Version:	1.4.2
Release:	1
Summary:	Slave process to perform risky IO

Group:		System Environment/Base
License:	GPLv2+
URL:		https://github.com/oVirt/ioprocess

# Note: the url fragment satisfies the build system, assuming that the source
# url ends with name-version.tar.gz. This part is ignored by the server.
# See https://fedoraproject.org/wiki/Packaging:SourceURL?rd=Packaging/SourceURL#Git_Tags
Source:		https://github.com/oVirt/ioprocess/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz


BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	glib2-devel
BuildRequires:	python3-devel
BuildRequires:	yajl-devel

Requires:	yajl


%description
Slave process to perform risky IO.


%prep
%setup -q %{name}-%{version}


%build
%configure
make %{?_smp_mflags}


%install
make %{?_smp_mflags} install DESTDIR="%{buildroot}"

%files
%{!?_licensedir:%global license %doc}
%{_libexecdir}/ioprocess
%doc README.md AUTHORS
%license COPYING

%package -n python3-ioprocess
Summary:	Python bindings for ioprocess
BuildRequires:	python3
BuildRequires:	python3-six
BuildRequires:	util-linux
Requires:	python3
Requires:	python3-six
Requires:	%{name} = %{version}

%description -n python3-ioprocess
Python bindings for ioprocess

%files -n python3-ioprocess
%{python3_sitelib}/ioprocess-*.egg-info
%{python3_sitelib}/ioprocess/
%doc README.md AUTHORS
%license COPYING


%changelog
* Tue Jul 06 2021 wangdi <wangdi@kylinos.cn> - 1.4.2-1
- Bump version to 1.4.2

* Thu Jun 24 2021 Xu Jin <jinxu@kylinos.cn> - 0.15.1-1
- Initial package for openEuler
