Summary:	GNU Bourne Again Shell (bash)
Summary(pl):	GNU Bourne Again Shell (bash)
Summary(de):	GNU Bourne Again Shell (bash)
Summary(fr):	GNU Bourne Again Shell (bash)
Summary(tr):	GNU Bourne Again Shell (bash)
Name:		bash
Version:	2.03
Release:	4
Group:		Shells
Group(pl):	Pow³oki
Copyright:	GPL
Source0:	ftp://prep.ai.mit.edu/pub/gnu/bash/%{name}-%{version}.tar.gz
Source1:	bashrc
Patch0:		bash-arm.patch
Patch1:		bash-fixes.patch
Patch2:		bash-paths.patch
Patch3:		bash-security.patch
Patch4:		bash-autoconf.patch
Patch5:		bash-info.patch
Prereq:		fileutils
Prereq:		grep
Prereq:		/sbin/install-info
BuildPrereq:	ncurses-devel
Buildroot:	/tmp/%{name}-%{version}-root
Obsoletes:	bash2

%description
Bash is an sh-compatible command language interpreter that
executes commands read from the standard input or from a
file.  Bash also incorporates useful features from the
Korn and C shells (ksh and csh).

Bash is ultimately intended to be a conformant implementation
of the IEEE Posix Shell and Tools specification (IEEE
Working Group 1003.2).

%description -l pl
Bash jest zaawansowanym shellem, który wykonuje komendy czytane ze
standardowego wej¶cia (stdin) lub z pliku. Posiada w³a¶ciwo¶ci 
shelli Korn i C (ksh i csh). 

Bash ma równie¿ zaimplementowany IEEE Posix Shell oraz jest zgodny ze 
specyfikacj± - IEEE Working Group 1003.2.

%description -l de
Bash ist ein sh-kompatibler Befehlssprachen-Interpreter, der
über die Standardeingabe oder eine Datei gelesene Befehle ausführt.
Bash beinhaltet außerdem nützliche Funktionen der Korn- und der
C-Shell (ksh und csh).

Bash soll eine kompatible Implementierung der
'IEEE Posix Shell and Tools Specification' (IEEE
Working Group 1003.2) sein.

%description -l fr
Bash est un interpréteur de commande compatible sh qui exécute
les commandes lues sur l'entrée standard ou depuis un fichier.
Bash inclue également des fonctionnalités utiles des shells Korn et C
(ksh et csh).

Bash est prévu pour être une implémentation de shell conforme la
spécification Posix IEEE sur les shell et les outils (Groupe de 
travail IEEE 1003.2).

%description -l tr
Bash standart giriþten ya da bir dosyadan komut okuyup çalýþtýran sh uyumlu
bir komut dili yorumlayýcýsýdýr. Ayný zamanda Korn ve C kabuklarýnýn (ksh ve
csh) kullanýþlý özelliklerini de kapsar. Bash, IEEE Posix Kabuk ve Araç
ayrýntýlarýna (IEEE Working Group 1003.2) uyumlu bir uygulama olarak
tasarlanmýþtýr.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
LDFLAGS="-s" CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr \
	--enable-alias \
	--enable-help-builtin \
	--enable-history \
	--enable-job-control \
	--enable-restricted \
	--enable-readline \
	--with-curses

make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{usr,bin,etc}
make prefix=$RPM_BUILD_ROOT/usr install

mv $RPM_BUILD_ROOT%{_bindir}/bash $RPM_BUILD_ROOT/bin/bash
rm -f $RPM_BUILD_ROOT%{_bindir}/installed-bash

rm -f $RPM_BUILD_ROOT%{_bindir}/bash.old

install %{SOURCE1} $RPM_BUILD_ROOT/etc/bashrc

echo .so bash.1 > $RPM_BUILD_ROOT%{_mandir}/man1/rbash.1

ln -sf bash $RPM_BUILD_ROOT/bin/rbash

gzip -9nf $RPM_BUILD_ROOT/usr/{info/bash.info,man/man1/*} \
	NEWS README 

%post
mv /etc/shells /etc/shells.org
(cat /etc/shells.org; echo "/bin/bash"; echo "/bin/rbash" ) | sort -u > /etc/shells
rm -f /etc/shells.org
/sbin/install-info %{_infodir}/bash.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	mv /etc/shells /etc/shells.org
	cat /etc/shells.org | egrep -v "/bin/bash|/bin/rbash" > /etc/shells
	rm -f /etc/shells.org
	/sbin/install-info --delete %{_infodir}/bash.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz

/etc/bashrc

%attr(755,root,root) /bin/*
%attr(755,root,root) %{_bindir}/*

%{_infodir}/bash.info.gz
%{_mandir}/man1/*

%changelog
* Mon May  3 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.03-4]
- added {un}registering info page for bash (added bash-info.patch).

* Mon Feb 22 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.03-1]
- removed /bin/sh link from bash (this is now provided by pdksh),
- removed man group from man pages,
- gzipping insterad bzipping2 man pages,
- rewrited %post, %preun,
- removed %config and %verify rules from /etc/bashrc (all extensions can be
  added by adding /etc/profile.d/*.sh scripts).

* Sun Sep 05 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.02.1-1d]
- fixed files permissions,
- build with restricted shell support.

* Wed Jun 17 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
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
