# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/colorwav
# catalog-date 2008-08-18 10:38:42 +0200
# catalog-license lgpl
# catalog-version 1.0
Name:		texlive-colorwav
Version:	1.0
Release:	11
Summary:	Colours by wavelength of visible light
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/colorwav
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorwav.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorwav.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorwav.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to obtain an RGB value (suitable
for use in the color package) from a wavelength of light. The
default unit is nanometres, but other units may be used. Note
that this function is also available within the xcolor.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/colorwav/colorwav.sty
%doc %{_texmfdistdir}/doc/latex/colorwav/README
%doc %{_texmfdistdir}/doc/latex/colorwav/colorwav.pdf
#- source
%doc %{_texmfdistdir}/source/latex/colorwav/colorwav.dtx
%doc %{_texmfdistdir}/source/latex/colorwav/colorwav.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 750377
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718101
- texlive-colorwav
- texlive-colorwav
- texlive-colorwav
- texlive-colorwav

