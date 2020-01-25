Name:  onedrive
Version:  2.3.13
Release:  1
Summary:  OneDrive Free Client written in D
License:  GPLv3
URL: https://github.com/abraunegg/onedrive
Source0:  https://github.com/abraunegg/onedrive/archive/v%{version}.tar.gz
BuildRequires:  ldc-dev
BuildRequires:  curl-dev
BuildRequires:  libnotify-dev
BuildRequires:  sqlite-autoconf-dev
BuildRequires:  systemd-dev
Requires(preun): systemd

%description
Free CLI client for Microsoft OneDrive written in D.

%prep
%setup -n %{name}-%{version}
sed -i 's/-o root -g users//g' Makefile.in
sed -i 's/-o root -g root//g' Makefile.in
# sed -i '/git/d' Makefile
sed -i "s|std\.c\.|core\.stdc\.|" src/sqlite.d
echo %{version} > version

%build
%configure

export PREFIX="%{_prefix}"
make PREFIX="%{_prefix}"

%install
%make_install PREFIX="%{_prefix}" 

%preun
systemctl --global disable %{name}.service
systemctl --no-reload disable --now %{name}@.service

%files
%license LICENSE 
/usr/bin/%{name}
/usr/lib/systemd/system/onedrive@.service
/usr/lib/systemd/user/onedrive.service
/usr/share/man/man1/onedrive.1
/usr/share/doc/onedrive/


%changelog
* Sat Jan 25 2020 David Va <davidva@tuta.io> - 2.3.13-1
- Update to 2.3.13 
- Cleaned spec file for CF

* Mon Aug 19 2019 David Va <davidva@tuta.io> - 2.3.8-1
- Update to 2.3.8 for bug fixes
