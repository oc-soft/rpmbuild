#
# spec file for package credential-ocs
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           credential-ocs
Version:       	0.1.0
Release:        1%{?dist}
Summary:        oc-soft crendential helper for git
License:        Apache-2.0
URL:           	https://oc-soft.net/credential-ocs 
Source0:       	credential-ocs-0.1.0.tar.gz 
Source1:        private-credential-ocs-0.1.0.tar.gz
BuildRequires:  gperf sqlite curl libjson-c-devel libcurl-devel sqlite3-devel libtool make npm



%description
OC-soft git crendential helper.
The credential helper generate bearer token, save and erase.

%prep
%setup -b 1

%conf
%configure --disable-hardcode-libs --disable-install-oclib

%build
%make_build LDFLAGS=-no-install

%install
%make_install SKIP_LOCPATH_INSTALL=yes

%post
echo '%{_datarootdir}/locale' > %{_libexecdir}/%name/locpath.txt

%files
%{_bindir}/%name
%{_libexecdir}/%name/*
%{_datarootdir}/locale/*/LC_MESSAGES/%name.mo

%changelog
* Tue Feb 28 2023 <toshi@oc-soft.net> - 0.1-1
- first release crendetial-ocs program.

# vi: se ts=4 sw=4 et:
