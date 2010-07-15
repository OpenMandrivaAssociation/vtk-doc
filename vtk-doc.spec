Name: vtk-doc
Version: 5.6.0
Release: %mkrel 1
License: BSD
Summary: Documentation for VTK %version
Group: Development/Other
URL: http://www.vtk.org/
Source0: http://www.vtk.org/doc/release/5.6/vtkDocHtml-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes: %{name}-docs < %{version}-%{release}
Provides: %{name}-docs = %{version}-%{release}

%description
Documentation for VTK %version.

%files 
%defattr(-,root,root,-)
%dir %_docdir/vtk
%_docdir/vtk/*

#-----------------------------------------

%install
rm -rf %buildroot
install -m 755 -d %buildroot/%_docdir/vtk
cd %buildroot/%_docdir/vtk
tar xfz %{SOURCE0}

%clean 
rm -rf %buildroot
