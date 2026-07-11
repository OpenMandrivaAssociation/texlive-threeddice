%global tl_name threeddice
%global tl_revision 20675

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Create images of dice with one, two, or three faces showing, using MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/threeddice
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/threeddice.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/threeddice.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides MetaPost code to create all possible symmetrical
views (up to rotation) of a right-handed die. Configuration is possible
by editing the source code, following the guidance in the documentation.

