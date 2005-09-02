Summary:	RenderMan-compatible renderer
Summary(pl):	Renderer kompatybilny z RenderManem
Name:		pixie
Version:	1.4.5
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/pixie/Pixie-src-%{version}.tgz
# Source0-md5:	51378b014fea28b2efa239aa4b74bda9
Patch0:		%{name}-destdir.patch
URL:		http://www.cs.berkeley.edu/~okan/Pixie/pixie.htm
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pixie is a RenderMan like photorealistic renderer. It is being
developed in the hope that it will be useful for graphics research and
for people who can not afford a commercial renderer.

%description -l pl
Pixie to fotorealistyczny renderer podobny do RenderMana. Jest
rozwijany z nadziej±, ¿e bêdzie przydatny do badañ nad grafik± i dla
ludzi, którzy nie mog± sobie pozwoliæ na komercyjny renderer.

%prep
%setup -q -n Pixie
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
