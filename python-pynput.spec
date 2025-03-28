Name:		python-pynput
Version:	1.8.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pynput/pynput-%{version}.tar.gz
Summary:	Monitor and control user input devices
URL:		https://pypi.org/project/pynput/
License:	LGPLv3
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Monitor and control user input devices

%files
%{py_sitedir}/pynput
%{py_sitedir}/pynput-*.*-info
