%global srcname FormEncode
Name:                python-%{srcname}
Version:             2.0.0
Release:             2
Summary:             HTML form validation, generation, and convertion package
License:             MIT and Python
URL:                 http://formencode.org/
Source0:             https://github.com/formencode/formencode/archive/refs/tags/2.0.0.tar.gz
BuildArch:           noarch
BuildRequires:        python3-pip python3-setuptools_scm_git_archive
%description
FormEncode validates and converts nested structures. It allows for a
declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%package -n python3-formencode
Summary:             HTML form validation, generation, and convertion package
BuildRequires:       python3-devel python3-setuptools python3-docutils
Requires:            python3-setuptools python-formencode-langpacks
%{?python_provide:%python_provide python3-formencode}
%description -n python3-formencode
FormEncode validates and converts nested structures. It allows for a
declarative form of defining the validation, and decoupled processes
for filling and generating forms.
This package contains the python3 version of the module.

%package -n python-formencode-langpacks
Summary:             Locale files for the python-formencode library
%description -n python-formencode-langpacks
The FormEncode library validates and converts nested structures.  This package
contains the locale files for localizing the message strings in code within the
library.

%prep
%setup -q -n formencode-%{version}
sed -i 's/use_scm_version=True,/use_scm_version=False,/g' setup.py

%build
%py3_build

%install
%py3_install
rm -rf $RPM_BUILD_ROOT%{python3_sitelib}/docs/
install -d -m 0755 $RPM_BUILD_ROOT%{python3_sitelib}/formencode/i18n
pushd formencode
  cp -arf i18n/* $RPM_BUILD_ROOT%{python3_sitelib}/formencode/i18n
popd 
for file in $RPM_BUILD_ROOT%{python3_sitelib}/formencode/i18n/* ; do
    if [ -d $file ] ; then
        if [ -e $file/LC_MESSAGES/%{srcname}.mo ] ; then
            mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/`basename $file`/LC_MESSAGES/
            mv $file/LC_MESSAGES/%{srcname}.mo $RPM_BUILD_ROOT%{_datadir}/locale/`basename $file`/LC_MESSAGES/
        fi
    fi
done
rm -rf $RPM_BUILD_ROOT%{python3_sitelib}/formencode/i18n
mv $RPM_BUILD_ROOT%{python3_sitelib}/%{srcname}-0.0.0-py%{python3_version}.egg-info $RPM_BUILD_ROOT%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
rm -rf $RPM_BUILD_ROOT/usr/LICENSE.txt
%find_lang %{srcname}

%files -n python3-formencode
%doc FormEncode.egg-info/PKG-INFO  LICENSE.txt docs
%{python3_sitelib}/formencode/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%files -n python-formencode-langpacks -f %{srcname}.lang

%changelog
* Wed May 18 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 2.0.0-2
- add necessary BuildRequires

* Wed May 26 2021 Ge Wang <wangge20@huawei.com> - 2.0.0-1
- Package init
