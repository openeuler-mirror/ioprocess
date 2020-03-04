# Note: this spec is used for RHEL, CentOS and Fedora. Plese do not use Fedora
# only macros. If you want to suggest changes please do this upstream:
# https://gerrit.ovirt.org/#/admin/projects/ioprocess

%global _configure ../configure


%if 0%{?rhel}
%if 0%{?rhel} < 8
%global with_python2 1
%global with_python3 0
%global python python
%else
%global with_python2 0
%global with_python3 1
%endif
%endif

%if 0%{?fedora}
%global with_python3 1
%if 0%{?fedora} < 30
%global with_python2 1
%global python python2
%else
%global with_python2 0
%endif
%endif

Name:		ioprocess
Version:	1.3.1
Release:	1%{?release_suffix}%{?dist}
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
BuildRequires:	glib2-devel
BuildRequires:	yajl-devel
Requires:	yajl

%if %with_python2
BuildRequires:	python2-devel
%endif

%if %with_python3
BuildRequires:	python3-devel
%endif


%description
Slave process to perform risky IO.


%prep
%setup -q %{name}-%{version}
mkdir py2 py3


%build
%if %with_python2
pushd py2
%configure PYTHON="%{__python2}"
make %{?_smp_mflags}
popd
%endif

%if %with_python3
pushd py3
%configure PYTHON="%{__python3}"
make %{?_smp_mflags}
popd
%endif


%install
%if 0%{?with_python2}
make -C py2 %{?_smp_mflags} install DESTDIR="%{buildroot}"
%endif # with_python2

%if 0%{?with_python3}
make -C py3 %{?_smp_mflags} install DESTDIR="%{buildroot}"
%endif # with_python3

%files
%{!?_licensedir:%global license %doc}
%{_libexecdir}/ioprocess
%doc README.md AUTHORS
%license COPYING

%if %with_python2
%package -n python2-ioprocess
Summary:	Python bindings for ioprocess
BuildRequires:	%{python}
BuildRequires:	%{python}-six
BuildRequires:	python-subprocess32
BuildRequires:	util-linux
Requires:	%{python}
Requires:	%{python}-six
Requires:	python-subprocess32
Requires:	%{name} = %{version}

# This package replaces python-ioprocess
Provides: python-ioprocess = %{version}
Obsoletes: python-ioprocess < %{version}

%description -n python2-ioprocess
Python bindings for ioprocess

%files -n python2-ioprocess
%{!?_licensedir:%global license %doc}
%{python2_sitelib}/ioprocess-*.egg-info
%{python2_sitelib}/ioprocess/
%doc README.md AUTHORS
%license COPYING
%endif

%if %with_python3
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
%endif


%changelog

* Tue Mar 03 2020 Huihui Fu <huihui.fu@cs2c.com.cn> 1.3.1-1
- Package Initialization
