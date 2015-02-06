Name:		meteor
Version:	1.4.0
Release:	2
Summary:	A GameBoy Advance emulator
License:	GPLv3+
Group:		Emulators
URL:		http://sourceforge.net/projects/meteorgba/
Source0:	http://sourceforge.net/projects/meteorgba/files/%{name}-%{version}.tar.bz2
Patch0:		meteor-1.4.0-gcc4.7.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	sfml-graphics-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glew)
BuildRequires:	nasm

%description
Meteor is a GameBoy Advance emulator with GTK2 frontend.

%prep
%setup -q
%patch0 -p1

%build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr
%make

%install
%makeinstall_std

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Meteor
Comment=GameBoy Advance emulator
Exec=%{_bindir}/%{name}
Icon=emulators_section
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Game;Emulator;
EOF

%files
%doc README COPYING AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop



%changelog
* Mon Mar 19 2012 Andrey Bondrov <abondrov@mandriva.org> 1.3.0-1mdv2012.0
+ Revision: 785545
- Update BuildRequires
- imported package meteor

