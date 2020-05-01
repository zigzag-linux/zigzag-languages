Name:           zigzag-languages
Version:        1.0.0
Release:        0
License:        GPL-3.0
Group:          System/Base
Summary:        Language packages installer
URL:            http://github.com/zigzag-linux/zigzag-languages
Source0:        %{name}-%{version}.tar.gz

Requires:       python3
Requires:       zypper
BuildArch:      noarch

%description
Utility script for finding and installing compatible language packages in
openSUSE ecosystem. Can execute on a cadence.

%prep
%autosetup

%build

%install
install -D -m 0755 zigzag_languages.py %{buildroot}%{_bindir}/zigzag-languages
install -d %{buildroot}%{_unitdir}
install -D -m 0644 etc/*.{service,timer} %{buildroot}%{_unitdir}

install -d %{buildroot}%{python3_sitelib}/zigzag_languages
cp zigzag_languages/* %{buildroot}%{python3_sitelib}/zigzag_languages

install -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rczigzag-languages

%pre
%service_add_pre zigzag-languages.service zigzag-languages.timer

%post
%service_add_post zigzag-languages.service zigzag-languages.timer

%preun
%service_del_preun zigzag-languages.service zigzag-languages.timer

%postun
%service_del_postun zigzag-languages.service zigzag-languages.timer

%files
%{_bindir}/zigzag-languages
%{_sbindir}/rczigzag-languages
%{_unitdir}/zigzag-*
%{python3_sitelib}/zigzag_languages

%changelog
