Summary:     GNU Bourne Again Shell (bash)
Summary(de): GNU Bourne Again Shell (bash)
Summary(fr): GNU Bourne Again Shell (bash)
Summary(pl): GNU Bourne Again Shell (bash)
Summary(tr): GNU Bourne Again Shell (bash)
Name:        bash
Version:     2.02.1
Release:     2
Group:       Shells
Copyright:   GPL
Source0:     ftp://ftp.gnu.org/pub/gnu/bash-%{PACKAGE_VERSION}.tar.gz
Source1:     bashrc
Source2:     rbash.1
Patch0:      bash-2.02-paths.patch
Patch1:      bash-2.02-security.patch
Patch2:      bash-fixes.patch
Prereq:      fileutils, grep 
BuildRoot:   /tmp/%{name}-%{version}-root

%description
Bash is an sh-compatible command language interpreter that executes commands
read from the standard input or from a file.  Bash also incorporates useful
features from the Korn and C shells (ksh and csh).

Bash is ultimately intended to be a conformant implementation of the IEEE
Posix Shell and Tools specification (IEEE Working Group 1003.2).

%description -l de
Bash ist ein sh-kompatibler Befehlssprachen-Interpreter, der über die
Standardeingabe oder eine Datei gelesene Befehle ausführt. Bash beinhaltet
außerdem nützliche Funktionen der Korn- und der C-Shell (ksh und csh).

Bash soll eine kompatible Implementierung der 'IEEE Posix Shell and Tools
Specification' (IEEE Working Group 1003.2) sein.

%description -l fr
Bash est un interpréteur de commande compatible sh qui exécute les commandes
lues sur l'entrée standard ou depuis un fichier. Bash inclue également des
fonctionnalités utiles des shells Korn et C (ksh et csh).

Bash est prévu pour être une implémentation de shell conforme la
spécification Posix IEEE sur les shell et les outils (Groupe de travail IEEE
1003.2).

%description -l pl
Bash jest zaawansowanym shellem, który wykonuje komendy czytane ze
standardowego wej¶cia (stdin) lub z pliku. Posiada w³a¶ciwo¶ci shelli: Korn
i C (ksh i csh).

Bash ma równie¿ zaimplementowany IEEE Posix Shell oraz jest zgodny ze
specyfikacj± - IEEE Working Group 1003.2.

%description -l tr
Bash standart giriþten ya da bir dosyadan komut okuyup çalýþtýran sh uyumlu
bir komut dili yorumlayýcýsýdýr. Ayný zamanda Korn ve C kabuklarýnýn (ksh ve
csh) kullanýþlý özelliklerini de kapsar. Bash, IEEE Posix Kabuk ve Araç
ayrýntýlarýna (IEEE Working Group 1003.2) uyumlu bir uygulama olarak
tasarlanmýþtýr.

%prep
%setup -q
%patch0 -p1 -b .paths
%patch1 -p1 -b .security
%patch2 -p1 -b .fixes

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" ./configure \
	--prefix=/usr \
	--with-curses \
	--enable-readline \
	--enable-history
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc,bin,usr/info}
make install prefix=$RPM_BUILD_ROOT/usr

mv $RPM_BUILD_ROOT/usr/bin/bash $RPM_BUILD_ROOT/bin
gzip -9nf $RPM_BUILD_ROOT/usr/info/bash.info*

install %{SOURCE1} $RPM_BUILD_ROOT/etc/bashrc

echo ".so bash.1" > $RPM_BUILD_ROOT/usr/man/man1/sh.1
ln -sf bash $RPM_BUILD_ROOT/bin/sh

install %{SOURCE2} $RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

# ***** bash doesn't use install-info. It's always listed in /usr/info/dir
# to prevent prereq loops
%post
if [ ! -f /etc/shells ]; then
	echo "/bin/bash" > /etc/shells
	echo "/bin/sh" >> /etc/shells
	echo "/bin/rbash" >> /etc/shells
else
	if ! grep '^/bin/bash$' /etc/shells > /dev/null; then
		echo "/bin/bash" >> /etc/shells
	fi
	if ! grep '^/bin/sh$' /etc/shells > /dev/null; then
		echo "/bin/sh" >> /etc/shells
	fi
	if ! grep '^/bin/rbash$' /etc/shells > /dev/null; then
		echo "/bin/rbash" >> /etc/shells
	fi
fi

%postun
if [ "$1" = "0" ]; then
	grep -v /bin/bash /etc/shells | grep -v /bin/sh | grep -v /bin/rbash> /etc/shells.new
	mv /etc/shells.new /etc/shells
fi

%files
%defattr(-,root,root)
%doc CHANGES COMPAT NEWS NOTES README CWRU/POSIX.NOTES
%doc doc/{FAQ,INTRO,article.ms}
%doc examples/{bashdb,functions,misc,scripts.noah,scripts.v2,scripts,startup-files}
%config /etc/bashrc
%attr(755, root, root) /bin/*
/usr/info/bash.info.gz
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Tue Oct  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.02.1-2]
- removed doc subpackage,
- added bash-fixes.patch (partialy based on Debian patch for bash) with
  following changes:
  - .bash_history created 600 by default,
  - bash binary is now linked with shared (system) libreadline, libhistory,
  - use TMPDIR by using tempnam(3),
  - man page with rbash(1),
- added symlink /bin/rbash -> bash and (un)registering in /etc/shells
  /bin/rbash in %post{un},
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- simplification in %install and %files,
- added %attr and %defattr macros in %files (allow build package from
  non-root account),
- added pl translation (Wojtek ¦lusarczyk <wojtek@shadow.eu.org>),
- added de, fr, tr translations from old 1.4.x bash spec.

* Wed Aug 19 1998 Jeff Johnson <jbj@redhat.com>
- resurrect for RH 6.0.

* Sun Jul 26 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.02.1

* Thu Jun 11 1998 Jeff Johnson <jbj@redhat.com>
- Package for 5.2.

* Mon Apr 20 1998 Ian Macdonald <ianmacd@xs4all.nl>
- added POSIX.NOTES doc file
- some extraneous doc files removed
- minor .spec file changes

* Sun Apr 19 1998 Ian Macdonald <ianmacd@xs4all.nl>
- upgraded to version 2.02
- Alpha, MIPS & Sparc patches removed due to lack of test platforms
- glibc & signal patches no longer required
- added documentation subpackage (doc)

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
