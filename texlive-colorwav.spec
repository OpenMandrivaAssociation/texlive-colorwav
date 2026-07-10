%global tl_name colorwav
%global tl_revision 67012

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Colours by wavelength of visible light
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/colorwav
License:	lgpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorwav.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorwav.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorwav.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the user to obtain an RGB value (suitable for use in
the color package) from a wavelength of light. The default unit is
nanometres, but other units may be used. Note that this function is also
available within xcolor.

