Name:		python-pynput
Version:	1.8.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pynput/pynput-%{version}.tar.gz
Source1:    %{name}-%{version}-eggs.tar.gz
Summary:	Monitor and control user input devices
URL:		https://pypi.org/project/pynput/
License:	LGPLv3
Group:		Development/Python
BuildArch:	noarch

BuildSystem:	python

BuildRequires:	python
BuildRequires:	python-xlib
BuildRequires:	python-evdev
BuildRequires:	python-six
BuildRequires:	python-twine
BuildRequires:	python-jinja2
BuildRequires:	python-nh3

%description
Monitor and control user input devices

%prep
%autosetup -n pynput-%{version} -p1
tar -zxf %{SOURCE1}

%files
%{py_sitedir}/pynput
%{py_sitedir}/pynput-*.*-info
