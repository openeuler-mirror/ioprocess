Name:		ioprocess
Version:	0.15.1
Release:	1
Summary:	Slave process to perform risky IO

Group:		System Environment/Base
License:	GPLv2+
URL:		https://github.com/oVirt/ioprocess
Source0:	https://github.com/oVirt/ioprocess/releases/tag/%{name}-%{version}.tar.gz


BuildRequires:	python3-devel
BuildRequires:	glib2-devel
BuildRequires:	yajl-devel
Requires:	yajl
Requires:	glib2 >= 2.28

%description
Slave process to perform risky IO.


%prep
%setup -q %{name}-%{version}


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%{!?_licensedir:%global license %doc}
%{_libexecdir}/ioprocess
%doc README.md AUTHORS
%license COPYING

%package -n python-ioprocess
Summary:	Python bindings for ioprocess
BuildArch:	noarch
Requires:	python
Requires:	python-cpopen
Requires:	python-six
Requires:	%{name} = %{version}-%{release}

%description -n python-ioprocess
Python bindings for ioprocess

%files -n python-ioprocess
%{!?_licensedir:%global license %doc}
%{python3_sitelib}/ioprocess-*.egg-info
%{python3_sitelib}/ioprocess/
%doc README.md AUTHORS
%license COPYING

%changelog
* Thu Jun 24 2021 Xu Jin <jinxu@kylinos.cn> - 0.15.1-1
- Initial package for openEuler
