Summary:	GNU Bourne Again Shell (bash)
Summary(de):	GNU Bourne Again Shell (bash)
Summary(fr):	Le shell Bourne Again de GNU
Summary(pl):	GNU Bourne Again Shell (bash)
Summary(tr):	GNU Bourne Again Shell (bash)
Name:		bash
Version:	2.04
Release:	12
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki
License:	GPL
Source0:	ftp://prep.ai.mit.edu/pub/gnu/bash/%{name}-%{version}.tar.gz
Source1:	%{name}rc
Source2:	%{name}-skel-.bash_logout
Source3:	%{name}-skel-.bash_profile
Source4:	%{name}-skel-.bashrc
Source5:	%{name}-skel_pl-.bashrc
Patch0:		%{name}-paths.patch
Patch1:		%{name}-fixes.patch
Patch2:		%{name}-security.patch
Patch3:		%{name}-autoconf.patch
Patch4:		%{name}-info.patch
Patch5:		%{name}-profile.patch
Patch6:		%{name}-requires.patch
Patch7:		%{name}-compat.patch
Patch8:		%{name}-shellfunc.patch
BuildRequires:	ncurses-static >= 5.0
BuildRequires:	readline-static >= 4.1
BuildRequires:	glibc-static
PreReq:		grep
PreReq:		fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	bash2
Obsoletes:	etcskel
Obsoletes:	bash2-doc

%description
Bash is a GNU project sh-compatible shell or command language
interpreter. Bash (Bourne Again shell) incorporates useful features
from the Korn shell (ksh) and the C shell (csh). Most sh scripts can
be run by bash without modification. Bash offers several improvements
over sh, including command line editing, unlimited size command
history, job control, shell functions and aliases, indexed arrays of
unlimited size and integer arithmetic in any base from two to 64. Bash
is ultimately intended to conform to the IEEE POSIX P1003.2/ISO 9945.2
Shell and Tools standard. Bash is the default shell for Linux
Mandrake. You should install bash because of its popularity and power.
You'll probably end up using it.

%description -l de
Bash ist eine sh-kompatible Shell und Kommandosprache aus dem
GNU-Projekt. Bash (Bourne Again Shell) vereinigt die nützlichen
Features aus der Korn-Shell (ksh) und der C-Shell (csh). Die meisten
sh-Skripte laufen ohne Änderungen auf bash. Bash hat viele
Erweiterungen im Vergleich zur "normalen" sh, wie z.B.
Kommandozeilenbearbeitung, unbeschränkte Größe der command-history,
Job-Kontrolle, Shell-Funktionen und -Aliase, unbegrenzt große
indizierte Arrays und Integer-Arithmetik in einer Basis von 2 bis 64.
Hauptziel von bash ist es, den IEEE POSIX P1003.2/ISO 9945.2 Shell-
und Tools-Standard einzuhalten. Bash ist die Standard-Shell für Linux
Mandrake.

%description -l fr
Bash est un shell (interpréteur de commande) du projet GNU, compatible
avec le shell historique sh. Bash (Bourne Again SHell) comprend de
nombreuses fonctionnalités du Korn SHell (ksh) et du C SHell (csh). La
plupart des scripts sh sont exécutables sans modifications. Bash
comprend nombre d'améliorations par rapport à sh : édition de la ligne
de commande, historique illimité, contrôle des processus
d'arrière-plan, fonctions de shell, alias, tableaux indexés de taille
illimitée et calcul sur des entiers dans n'importe quelle base de 2 à
64. Bash est conforme au standard IEEE POSIX P1003.2/ISO 9945.2 Shell
and Tools. Bash est le shell par défaut de Mandrake. Vous devriez
l'installer du fait de sa puissance et de sa popularité. Vous finirez
probablement par l'utiliser.

%description -l pl
Bash jest zaawansowanym shellem, który wykonuje komendy czytane ze
standardowego wej¶cia (stdin) lub z pliku. Posiada w³a¶ciwo¶ci shelli
Korn i C (ksh i csh). Bash ma równie¿ zaimplementowany IEEE Posix
Shell oraz jest zgodny ze specyfikacj± - IEEE Working Group 1003.2.

%description -l tr
Bash standart giriþten ya da bir dosyadan komut okuyup çalýþtýran sh
uyumlu bir komut dili yorumlayýcýsýdýr. Ayný zamanda Korn ve C
kabuklarýnýn (ksh ve csh) kullanýþlý özelliklerini de kapsar. Bash,
IEEE Posix Kabuk ve Araç ayrýntýlarýna (IEEE Working Group 1003.2)
uyumlu bir uygulama olarak tasarlanmýþtýr.

%package static
Summary:	Staticly linked GNU Bourne Again Shell (bash)
Summary(pl):	Statycznie zlinkowany GNU Bourne Again Shell (bash)
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki
Requires:	%{name}
PreReq:		grep
PreReq:		fileutils

%description static
Bash is a GNU project sh-compatible shell or command language
interpreter. Bash (Bourne Again shell) incorporates useful features
from the Korn shell (ksh) and the C shell (csh). Most sh scripts can
be run by bash without modification. Bash offers several improvements
over sh, including command line editing, unlimited size command
history, job control, shell functions and aliases, indexed arrays of
unlimited size and integer arithmetic in any base from two to 64. Bash
is ultimately intended to conform to the IEEE POSIX P1003.2/ISO 9945.2
Shell and Tools standard. Bash is the default shell for Linux
Mandrake. You should install bash because of its popularity and power.
You'll probably end up using it. This packege contains staticly linked
version of bash.

%description static -l pl
Bash jest zaawansowanym shellem, który wykonuje komendy czytane ze
standardowego wej¶cia (stdin) lub z pliku. Posiada w³a¶ciwo¶ci shelli
Korn i C (ksh i csh). Bash ma równie¿ zaimplementowany IEEE Posix
Shell oraz jest zgodny ze specyfikacj± - IEEE Working Group 1003.2. W
tym pakiecie jest statycznie zlinkowany bash.

%prep
%setup	-q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

echo %{version} > _distribution
echo %{release} > _patchlevel

%build
%configure \
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
	--with-installed-readline

%{__make} TERMCAP_LIB="-ltinfo"
mv -f bash bash.static
%{__make} TERMCAP_LIB="-ltinfo" STATIC_LD=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_infodir}} \
	$RPM_BUILD_ROOT/{bin,etc/skel/{C,pl}}

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} 

mv -f $RPM_BUILD_ROOT%{_bindir}/bash $RPM_BUILD_ROOT/bin
install	bash.static $RPM_BUILD_ROOT/bin

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/bashrc
echo .so bash.1 > $RPM_BUILD_ROOT%{_mandir}/man1/rbash.1

ln -sf bash $RPM_BUILD_ROOT/bin/rbash

install %{SOURCE2} $RPM_BUILD_ROOT/etc/skel/C/.bash_logout
install %{SOURCE3} $RPM_BUILD_ROOT/etc/skel/C/.bash_profile
install %{SOURCE4} $RPM_BUILD_ROOT/etc/skel/C/.bashrc
install %{SOURCE5} $RPM_BUILD_ROOT/etc/skel/pl/.bashrc

gzip -9nf NEWS README doc/{FAQ,INTRO}
gzip -9nf $RPM_BUILD_ROOT%{_infodir}/bash.info

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

[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post static
if [ ! -f /etc/shells ]; then
	echo "/bin/bash.static" > /etc/shells
else
	if ! grep '^/bin/bash.static$' /etc/shells > /dev/null; then
		echo "/bin/bash.static" >> /etc/shells
	fi
fi

%preun
if [ "$1" = "0" ]; then
	grep -v /bin/bash /etc/shells | grep -v /bin/rbash > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%preun static
if [ "$1" = "0" ]; then
	grep -v /bin/bash.static /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz doc/{FAQ,INTRO}.gz

%config %{_sysconfdir}/bashrc

/etc/skel/C/.bash_logout
/etc/skel/C/.bash_profile
/etc/skel/C/.bashrc
%lang(pl) /etc/skel/pl/.bashrc

%attr(755,root,root) /bin/bash
%attr(755,root,root) /bin/rbash
%attr(755,root,root) %{_bindir}/bashbug

%{_infodir}/bash.info.gz
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) /bin/bash.static
