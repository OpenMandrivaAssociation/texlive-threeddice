Name:		texlive-threeddice
Version:	20675
Release:	2
Summary:	Create images of dice with one, two, or three faces showing, using MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/threeddice
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/threeddice.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/threeddice.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides MetaPost code to create all possible
symmetrical views (up to rotation) of a right-handed die.
Configuration is possible by editing the source code, following
the guidance in the documentation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/threeddice/threeddice.mp
%doc %{_texmfdistdir}/doc/metapost/threeddice/README
%doc %{_texmfdistdir}/doc/metapost/threeddice/threeddice-doc.pdf
%doc %{_texmfdistdir}/doc/metapost/threeddice/threeddice-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
