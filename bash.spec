Summary:	GNU Bourne Again Shell (bash)
Summary(pl):	GNU Bourne Again Shell (bash)
Summary(de):	GNU Bourne Again Shell (bash)
Summary(fr):	GNU Bourne Again Shell (bash)
Summary(tr):	GNU Bourne Again Shell (bash)
Name:		bash
Version:	2.03
Release:	1
Group:		Shells
Copyright:	GPL
Source0:	ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Source1:	bashrc
Patch0:		%{name}.patch
Patch1:		%{name}-fixes.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-security.patch
Prereq:		fileutils
Prereq:		grep 
Buildroot:	/tmp/%{name}-%{version}-root

%description
Bash is an sh-compatible command language interpreter that
executes commands read from the standard input or from a
file.  Bash also incorporates useful features from the
Korn and C shells (ksh and csh).

Bash is ultimately intended to be a conformant implementation
of the IEEE Posix Shell and Tools specification (IEEE
Working Group 1003.2).

%description -l pl
Bash jest zaawansowanym shellem, kt�ry wykonuje komendy czytane ze
standardowego wej�cia (stdin) lub z pliku. Posiada w�a�ciwo�ci 
shelli Korn i C (ksh i csh). 

Bash ma r�wnie� zaimplementowany IEEE Posix Shell oraz jest zgodny ze 
specyfikacj� - IEEE Working Group 1003.2.

%description -l de
Bash ist ein sh-kompatibler Befehlssprachen-Interpreter, der
�ber die Standardeingabe oder eine Datei gelesene Befehle ausf�hrt.
Bash beinhaltet au�erdem n�tzliche Funktionen der Korn- und der
C-Shell (ksh und csh).

Bash soll eine kompatible Implementierung der
'IEEE Posix Shell and Tools Specification' (IEEE
Working Group 1003.2) sein.

%description -l fr
Bash est un interpr�teur de commande compatible sh qui ex�cute
les commandes lues sur l'entr�e standard ou depuis un fichier.
Bash inclue �galement des fonctionnalit�s utiles des shells Korn et C
(ksh et csh).

Bash est pr�vu pour �tre une impl�mentation de shell conforme la
sp�cification Posix IEEE sur les shell et les outils (Groupe de 
travail IEEE 1003.2).

%description -l tr
Bash standart giri�ten ya da bir dosyadan komut okuyup �al��t�ran sh uyumlu
bir komut dili yorumlay�c�s�d�r. Ayn� zamanda Korn ve C kabuklar�n�n (ksh ve
csh) kullan��l� �zelliklerini de kapsar. Bash, IEEE Posix Kabuk ve Ara�
ayr�nt�lar�na (IEEE Working Group 1003.2) uyumlu bir uygulama olarak
tasarlanm��t�r.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
LDFLAGS="-s" CFLAGS="$RPM_OPT_FLAGS" \
./configure \
	--prefix=/usr \
	--enable-alias \
	--enable-help-builtin \
	--enable-history \
	--enable-job-control \
	--enable-restricted \
	--enable-readline \
	--enable-static-link
make 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{usr,bin,etc}
make prefix=$RPM_BUILD_ROOT/usr install

mv $RPM_BUILD_ROOT/usr/bin/bash $RPM_BUILD_ROOT/bin/bash
rm -f $RPM_BUILD_ROOT/usr/bin/installed-bash

rm -f $RPM_BUILD_ROOT/usr/bin/bash.old

install %{SOURCE1} $RPM_BUILD_ROOT/etc/bashrc

echo .so bash.1 > $RPM_BUILD_ROOT/usr/man/man1/sh.1
echo .so bash.1 > $RPM_BUILD_ROOT/usr/man/man1/rbash.1

ln -sf bash $RPM_BUILD_ROOT/bin/sh
ln -sf bash $RPM_BUILD_ROOT/bin/rbash

gzip -9nf $RPM_BUILD_ROOT/usr/{info/bash.info,man/man1/*}

bzip2 -9 NEWS README 

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cat /etc/shells; echo "/bin/sh"; echo "/bin/bash"; echo "/bin/rbash") | sort -u > /etc/shells

%preun
cat /etc/shells | egrep -v "/bin/bash|/bin/bash|/bin/rbash" > /etc/shells

%files
%defattr(644,root,root,755)
%doc NEWS.bz2 README.bz2 

/etc/bashrc

%attr(755,root,root) /bin/*
%attr(755,root,root) /usr/bin/*

/usr/info/bash.info.gz
/usr/man/man1/*

%changelog
* Mon Feb 22 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.03-1]
- removed man group from man pages,
- gzipping insterad bzipping2 man pages,
- rewrited %post, %preun,
- removed %config and %verify rules from /etc/bashrc (all extensions can be
  added by adding /etc/profile.d/*.sh scripts).

* Sun Sep 05 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [2.02.1-1d]
- updated to 2.02.1,
- fixed files permissions,
- build with restricted shell support.

* Wed Jun 17 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [14.7-9d]
- build against glibc-2.1,
- translation modified for pl,
- added %defattr support,
- build from non root's account.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Nov 07 1997 Donnie Barnes <djb@redhat.com>
- added signal handling patch from Dean Gaudet <dgaudet@arctic.org> that
  is based on a change made in bash 2.0.  Should fix some early exit
  problems with suspends and fg.

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- added %clean

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- added comment explaining why install-info isn't used
- added mips patch 

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added BuildRoot

* Tue Jun 03 1997 Erik Troan <ewt@redhat.com>
- built against glibc
