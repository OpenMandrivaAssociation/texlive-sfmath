# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sfmath/sfmath.sty
# catalog-date 2008-08-23 15:48:35 +0200
# catalog-license lppl
# catalog-version 0.8
Name:		texlive-sfmath
Version:	0.8
Release:	7
Summary:	Sans-serif mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sfmath/sfmath.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sfmath.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
sfmath is a simple package for sans serif maths in documents.
After including the package, all maths of the current document
is displayed with sans serif fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sfmath/sfmath.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.8-2
+ Revision: 755968
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.8-1
+ Revision: 719518
- texlive-sfmath
- texlive-sfmath
- texlive-sfmath
- texlive-sfmath

