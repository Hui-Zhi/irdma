#
# spec file for package intel-irdma (Version 2.0.7)
#
# Copyright (c) 2021 SUSE Software Solutions Germany GmbH
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Name: intel-irdma
Summary: Intel(R) Ethernet Connection RDMA Driver
Version: 2.0.7
Release: 0
Source0: irdma-%{version}.tgz
Group: System/Kernel
License: GPL-2.0 or BSD-2-Clause
BuildRequires: %kernel_module_package_buildreqs
%if 0%{?sle_version} < 150400
BuildRequires:  intel-auxiliary-devel
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-build


%kernel_module_package

%description
This package contains the Intel(R) Ethernet Connection RDMA Driver


%prep
%setup -q -n irdma-%{version}
set -- *
mkdir source
mv "$@" source/
echo "irdma.ko external" > source/src/irdma/Module.supported
mkdir obj


%build
for flavor in %flavors_to_build; do
    rm -rf obj/$flavor
    cp -r source obj/$flavor
    pushd $PWD/obj/$flavor
    export KSRC=%{kernel_source $flavor}
    ./build.sh noofed noinstall
    popd
done


%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=%kernel_module_package_moddir
for flavor in %flavors_to_build; do
    make -C %{kernel_source $flavor} modules_install M=$PWD/obj/$flavor/src/irdma
done


%clean
rm -rf %{buildroot}

%changelog
* Tue May  6 2025 donald.buchholz@intel.com
- version: 2.0.7 (Release 30.2)
* Thu Apr 24 2025 hui.zhi.zhao@suse.com
- version: 1.17.31 bsc#1241665 (Release 30.1)
* Thu Apr 10 2025 donald.buchholz@intel.com
- version: 1.17.31 (Dell Everglades X03)
* Tue Feb 25 2025 donald.buchholz@intel.com
- version: 1.17.25 (Dell Everglades X01)
* Tue Feb 25 2025 donald.buchholz@intel.com
- version: 1.16.10
- Merging changes (including SUSE's comments) from the SolidDriver SPEC files
  supporting Release 30.0.1 in preparation for Dell_Everglades X01.
* Wed Feb 19 2025 hui.zhi.zhao@suse.com
- version: 1.16.11 bsc#1237333
* Thu Dec 12 2024 hui.zhi.zhao@suse.com
- version: 1.16.10 bsc#1234387
* Fri Dec  6 2024 hui.zhi.zhao@suse.com
- version: 1.15.11 bsc#1234262
* Mon Nov  4 2024 hui.zhi.zhao@suse.com
- version: 1.15.12 bsc#1232736
* Thu Sep 12 2024 hui.zhi.zhao@suse.com
- version: 1.15.7 bsc#1230465
* Mon Jul  1 2024 hui.zhi.zhao@suse.com
- version: 1.14.32 bsc#1227189
* Tue Jun 11 2024 donald.buchholz@intel.com
- version: 1.14.32 (Dell Dante X06)
* Thu May  9 2024 hui.zhi.zhao@suse.com
- version: 1.14.17 bsc#1224031
* Mon May  6 2024 hui.zhi.zhao@suse.com
- version: 1.13.43 bsc#1223612
* Fri Apr 26 2024 donald.buchholz@intel.com
- version: 1.13.43 (Release 28.3 & Release 29.0)
* Wed Aug  9 2023 hui.zhi.zhao@suse.com
- version: 1.12.55 bsc#1214092  (Dell Crockett A00)
* Mon Feb 20 2023 hui.zhi.zhao@suse.com
- version: 1.11.58 bsc#1208475
* Wed Aug  3 2022 hui.zhi.zhao@suse.com
- Add auxiliary bus dep back
* Wed Aug  3 2022 hui.zhi.zhao@suse.com
- remove auxiliary bus deps
* Wed Aug  3 2022 hui.zhi.zhao@suse.com
- Version: 1.9.30 bsc#1202080
* Fri May 27 2022 hui.zhi.zhao@suse.com
- Version: 1.8.46 bsc#1199933
* Wed Mar  9 2022 hui.zhi.zhao@suse.com
- Version: 1.8.45 bsc#1196820
* Mon Feb 28 2022 hui.zhi.zhao@suse.com
- version 1.7.72 bsc#1196532
* Thu Jul  1 2021 lance.ortiz@suse.com
- version 1.6.28 bsc#1187899
* Tue Jan 19 2021 lance.ortiz@suse.com
- version 1.2.21 bsc#1180941
* Thu Aug  6 2020 lance.ortiz@suse.com
- initial version 1.0.13 (bsc#1174876)
