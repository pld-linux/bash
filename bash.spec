Summary:	GNU Bourne Again Shell (bash)
Summary(pl):	GNU Bourne Again Shell (bash)
Summary(de):	GNU Bourne Again Shell (bash)
Summary(fr):	GNU Bourne Again Shell (bash)
Summary(tr):	GNU Bourne Again Shell (bash)
Name:		bash
Version:	2.03
Release:	7
Group:		Shells
Group(pl):	Pow³oki
Copyright:	GPL
Source0:	ftp://prep.ai.mit.edu/pub/gnu/bash/%{name}-%{version}.tar.gz
Source1:	bashrc
Source2:	bash-extra.tar.bz2
Patch0:		bash-arm.patch
Patch1:		bash-fixes.patch
Patch2:		bash-paths.patch
Patch3:		bash-security.patch
Patch4:		bash-autoconf.patch
Patch5:		bash-info.patch
BuildPrereq:	ncurses-devel
PreRequires:	/sbin/install-info
PreRequires:	grep
PreRequires:	/bin/mv
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

%package static
Summary:	Staticly linked GNU Bourne Again Shell (bash)
Summary(pl):	Statycznie zlinkowany GNU Bourne Again Shell (bash)
Group:		Shells
Group(pl):	Pow³oki
Requires:	%{name}

%description static
Bash is an sh-compatible command language interpreter that
executes commands read from the standard input or from a
file.  Bash also incorporates useful features from the
Korn and C shells (ksh and csh).

Bash is ultimately intended to be a conformant implementation
of the IEEE Posix Shell and Tools specification (IEEE
Working Group 1003.2).

This packege contains staticly linked version of bash.

%description static -l pl
Bash jest zaawansowanym shellem, który wykonuje komendy czytane ze
standardowego wej¶cia (stdin) lub z pliku. Posiada w³a¶ciwo¶ci 
shelli Korn i C (ksh i csh). 

Bash ma równie¿ zaimplementowany IEEE Posix Shell oraz jest zgodny ze 
specyfikacj± - IEEE Working Group 1003.2.

W tym pakiecie jest statycznie zlinkowany bash.

%prep
%setup	-q -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=%{_prefix} \
	--enable-alias \
	--enable-help-builtin \
	--enable-history \
	--enable-job-control \
	--enable-restricted \
	--enable-readline \
	--with-curses \
	--enable-extended-glob \
	--enable-dparen-arithmetic \
	--enable-static-link \
	--infodir=%{_infodir} \
	%{_target_platform}

make TERMCAP_LIB="-lncurses"
mv bash bash.static
make TERMCAP_LIB="-lncurses" STATIC_LD=""

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_mandir},%{_infodir}}
install -d $RPM_BUILD_ROOT/{bin,etc}

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} 

mv $RPM_BUILD_ROOT%{_bindir}/bash	$RPM_BUILD_ROOT/bin
install	-s bash.static	$RPM_BUILD_ROOT/bin

install	%{SOURCE1}	$RPM_BUILD_ROOT/etc/bashrc
cp -a	skel		$RPM_BUILD_ROOT/etc
echo	.so bash.1 >	$RPM_BUILD_ROOT%{_mandir}/man1/rbash.1
ln -sf	bash		$RPM_BUILD_ROOT/bin/rbash

gzip -9nf	$RPM_BUILD_ROOT{%{_infodir}/bash.info,%{_mandir}/man1/*} \
		NEWS README doc/{FAQ,INTRO}

%post
if [ ! -f /etc/shells ]; then
	echo "/bin/bash" > /etc/shells
	echo "/bin/rbash" >> /etc/shells
else
	if ! grep '^/bin/bash$' /etc/shells > /dev/null; then
		echo "/bin/bash" >> /etc/shells
	fi
	if ! grep '^/bin/rbash$' /etc/shells > /dev/null; then
		echo "/bin/rbash" >> /etc/shells
	fi

fi

/sbin/install-info %{_infodir}/bash.info.gz /etc/info-dir

%post static
if [ ! -f /etc/shells ]; then
	echo "/bin/bash.static" > /etc/shells
else
	if ! grep '^/bin/bash.static$' /etc/shells > /dev/null; then
		echo "/bin/bash.static" >> /etc/shells
	fi
fi

%preun
if [ $1 = 0 ]; then
	grep -v /bin/bash /etc/shells | grep -v /bin/rbash > /etc/shells.new
	mv /etc/shells.new /etc/shells
fi

/sbin/install-info --delete %{_infodir}/bash.info.gz /etc/info-dir

%preun static
if [ $1 = 0 ]; then
	grep -v /bin/bash.static /etc/shells > /etc/shells.new
	mv /etc/shells.new /etc/shells
fi


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz doc/{FAQ,INTRO}.gz

/etc/bashrc
/etc/skel

%attr(755,root,root) /bin/bash
%attr(755,root,root) /bin/rbash
%attr(755,root,root) %{_bindir}/bashbug

%{_infodir}/bash.info.gz
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) /bin/bash

%changelog
* Sat Jun  5 1999 Jan Rêkorajski <baggins@pld.org.pl>
  [2.03-7]
- added static subpackage

* Wed May 19 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.03-5]
- more macros,
- FHS 2.0.

* Mon May  3 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.03-4]
- added {un}registering info page for bash (added bash-info.patch).

* Mon Feb 22 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.03-1]
- removed /bin/sh link from bash (this is now provided by pdksh),
- removed man group from man pages,
- gzipping instead bzipping2 man pages,
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
- build from non root's account,
- start at RH spec.
