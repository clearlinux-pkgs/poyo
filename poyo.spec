#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : poyo
Version  : 0.5.0
Release  : 7
URL      : https://files.pythonhosted.org/packages/7d/56/01b496f36bbd496aed9351dd1b06cf57fd2f5028480a87adbcf7a4ff1f65/poyo-0.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/7d/56/01b496f36bbd496aed9351dd1b06cf57fd2f5028480a87adbcf7a4ff1f65/poyo-0.5.0.tar.gz
Summary  : A lightweight YAML Parser for Python. 🐓
Group    : Development/Tools
License  : MIT
Requires: poyo-python = %{version}-%{release}
Requires: poyo-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
A lightweight YAML Parser for Python. 🐓
        
        **poyo** does not allow deserialization of arbitrary Python objects. Supported
        types are `str`, `bool`, `int`, `float`, `NoneType` as well as `dict` and
        `list` values.
        
        ⚠️ Please note that poyo supports only a chosen subset of the YAML format
        that is required to parse [cookiecutter user configuration
        files][cookiecutterrc]. poyo does not have support for serializing into YAML
        and is not compatible with JSON.

%package python
Summary: python components for the poyo package.
Group: Default
Requires: poyo-python3 = %{version}-%{release}

%description python
python components for the poyo package.


%package python3
Summary: python3 components for the poyo package.
Group: Default
Requires: python3-core
Provides: pypi(poyo)

%description python3
python3 components for the poyo package.


%prep
%setup -q -n poyo-0.5.0
cd %{_builddir}/poyo-0.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623345896
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
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
