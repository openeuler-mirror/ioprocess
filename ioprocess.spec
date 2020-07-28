# Note: this spec is used for RHEL, CentOS and Fedora. Plese do not use Fedora
# only macros. If you want to suggest changes please do this upstream:
# https://gerrit.ovirt.org/#/admin/projects/ioprocess

Name:		ioprocess
Version:	1.4.1
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
Tue Jul 28 2020 jiangxinyu <jiangxinyu@kylinos.cn> - 1.4.0-1
- Init ioprocess project
