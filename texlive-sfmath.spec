# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sfmath/sfmath.sty
# catalog-date 2008-08-23 15:48:35 +0200
# catalog-license lppl
# catalog-version 0.8
Name:		texlive-sfmath
Version:	0.8
Release:	1
Summary:	Sans-serif mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sfmath/sfmath.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sfmath.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
sfmath is a simple package for sans serif maths in documents.
After including the package, all maths of the current document
is displayed with sans serif fonts.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
