Name:		texlive-sfmath
Version:	15878
Release:	1
Summary:	Sans-serif mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sfmath/sfmath.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sfmath.r%{version}.tar.xz
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
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
