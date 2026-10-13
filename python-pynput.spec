Name:		python-pynput
Version:	1.8.1
Release:	4
Source0:	https://files.pythonhosted.org/packages/source/p/pynput/pynput-%{version}.tar.gz
Source1:    %{name}-%{version}-eggs.tar.gz
Summary:	Monitor and control user input devices
URL:		https://pypi.org/project/pynput/
License:	LGPLv3
Group:		Development/Python
BuildArch:	noarch

BuildSystem:	python

BuildRequires:	python
BuildRequires:	python%{pyver}dist(python-xlib)
BuildRequires:	python%{pyver}dist(evdev)
BuildRequires:	python%{pyver}dist(six)
BuildRequires:	python%{pyver}dist(jinja2)
BuildRequires:	python%{pyver}dist(nh3)

%description
Monitor and control user input devices

%prep
%autosetup -n pynput-%{version} -p1
tar -zxf %{SOURCE1}

%files
%{py_sitedir}/pynput
%{py_sitedir}/pynput-*.*-info
