#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jaraco.classes
Version  : 3.2.1
Release  : 10
URL      : https://files.pythonhosted.org/packages/7b/de/28a640c17a80f5e0fab5c494679e2e66b36d7fd20622e27718bea8be34b8/jaraco.classes-3.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/7b/de/28a640c17a80f5e0fab5c494679e2e66b36d7fd20622e27718bea8be34b8/jaraco.classes-3.2.1.tar.gz
Summary  : Utility functions for Python class constructs
Group    : Development/Tools
License  : MIT
Requires: jaraco.classes-license = %{version}-%{release}
Requires: jaraco.classes-python = %{version}-%{release}
Requires: jaraco.classes-python3 = %{version}-%{release}
Requires: more-itertools
BuildRequires : buildreq-distutils3
BuildRequires : more-itertools
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : setuptools_scm-python
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/jaraco.classes.svg
:target: `PyPI link`_

%package license
Summary: license components for the jaraco.classes package.
Group: Default

%description license
license components for the jaraco.classes package.


%package python
Summary: python components for the jaraco.classes package.
Group: Default
Requires: jaraco.classes-python3 = %{version}-%{release}

%description python
python components for the jaraco.classes package.


%package python3
Summary: python3 components for the jaraco.classes package.
Group: Default
Requires: python3-core
Provides: pypi(jaraco.classes)
Requires: pypi(more_itertools)

%description python3
python3 components for the jaraco.classes package.


%prep
%setup -q -n jaraco.classes-3.2.1
cd %{_builddir}/jaraco.classes-3.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619115835
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jaraco.classes
cp %{_builddir}/jaraco.classes-3.2.1/LICENSE %{buildroot}/usr/share/package-licenses/jaraco.classes/8e6689d37f82d5617b7f7f7232c94024d41066d1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3.*/site-packages/jaraco/__init__.py
rm -f %{buildroot}/usr/lib/python3.*/site-packages/jaraco/__pycache__/__init__.*

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jaraco.classes/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
