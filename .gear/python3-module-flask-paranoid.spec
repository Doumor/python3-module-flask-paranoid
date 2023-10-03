%define pypi_name flask-paranoid

%def_enable check

Name:    python3-module-%pypi_name
Version: 0.3.0
Release: alt1

Summary: Simple user session protection
License: MIT
Group:   Development/Python3
URL:     https://github.com/miguelgrinberg/flask-paranoid

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-flask python3-module-pytest

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir/flask_paranoid/
%python3_sitelibdir/Flask_Paranoid-%version.dist-info

%changelog
* Wed Oct 04 2023 Danilkin Danila <danild@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
