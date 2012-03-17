Name:		meteor
Version:	1.3.0
Release:	%mkrel 1
Summary:	A GameBoy Advance emulator
License:	GPLv3+
Group:		Emulators
URL:		http://sourceforge.net/projects/meteorgba/
Source0:	http://sourceforge.net/projects/meteorgba/files/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	gtk2-devel >= 2.24
BuildRequires:	gtkmm2.4-devel
BuildRequires:	sfml-graphics-devel
BuildRequires:	X11-devel
BuildRequires:	nasm

%description
Meteor is a GameBoy Advance emulator with GTK2 frontend.

%prep
%setup -q

%build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr
%make

%install
%__rm -rf %{buildroot}
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

%clean
%__rm -rf %{buildroot}

%files
%doc README COPYING AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

