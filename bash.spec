Summary:	GNU Bourne Again Shell (bash)
Summary(fr):	Le shell Bourne Again de GNU
Name:		bash
Version:	2.05
Release:	9
License:	GPL
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki
Source0:	ftp://prep.ai.mit.edu/pub/gnu/bash/%{name}-%{version}.tar.gz
Source1:	%{name}rc
Source2:	%{name}-skel-.bash_logout
Source3:	%{name}-skel-.bash_profile
Source4:	%{name}-skel-.bashrc
Source5:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-paths.patch
Patch1:		%{name}-security.patch
Patch2:		%{name}-autoconf.patch
Patch3:		%{name}-info.patch
Patch4:		%{name}-profile.patch
Patch5:		%{name}-requires.patch
Patch6:		%{name}-compat.patch
Patch7:		%{name}-shellfunc.patch
Patch8:		http://www.t17.ds.pwr.wroc.pl/~misiek/ipv6/bash-2.05-ipv6-20010418.patch.gz
Patch9:		%{name}-DESTDIR.patch
Patch10:	%{name}-rlimit_locks.patch
Patch11:	%{name}-sighup.patch
Patch12:	%{name}-tmpfile.patch
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	glibc-devel >= 2.2
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
BiuldRequires:  texinfo
%if %{!?_without_static:1}%{?_without_static:0}
# Require static library only for static build
BuildRequires:	glibc-static >= 2.2
BuildRequires:	ncurses-static >= 5.2
BuildRequires:	readline-static >= 4.2
%endif
Prereq:		grep
Prereq:		fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	bash-doc
Obsoletes:	bash2
Obsoletes:	bash2-doc
Obsoletes:	etcskel

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
Bash (Bourne Again SHell) jest projektem GNU pow³oki kompatybilnej z
sh oraz interpretera jêzyka poleceñ. Posiada u¿yteczne w³a¶ciwo¶ci
pow³ok Korn (ksh) i C (csh). Wiêkszo¶æ skryptów sh mo¿e byæ
uruchamiana w bashu bez modyfikacji. Oferuje on kilka ulepszeñ w
stusunku do sh, w³±czaj±c edycjê linii poleceñ, nieograniczony rozmiar
historii poleceñ, funkcje i aliasy, indeksowane tablice
nieograniczonych rozmiarów oraz arytmetykê ca³kowitoliczbow± o
dowolnej podstawie od 2 do 64. W zamierzeniu ostatecznie ma byæ zgodny
ze standardem IEEE POSIX P1003.2/ISO 9945.2 Shell and Tools.

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
Prereq:		grep
Prereq:		fileutils

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
You'll probably end up using it. This packege contains statically
linked version of bash.

%description static -l pl
Bash jest zaawansowanym shellem, który wykonuje komendy czytane ze
standardowego wej¶cia (stdin) lub z pliku. Posiada w³a¶ciwo¶ci pow³ok
Korn i C (ksh i csh). Bash ma równie¿ zaimplementowany IEEE Posix
Shell oraz jest zgodny ze specyfikacj± - IEEE Working Group 1003.2. W
tym pakiecie jest statycznie zlinkowany bash.

%prep
%setup -q -a5
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

echo %{version} > _distribution
echo %{release} > _patchlevel

%build
autoconf
for mode in %{!?_without_static:static} shared; do
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
	`[ "$mode" = "static" ] && echo "--enable-static-link"` \
	--with-installed-readline

%{__make} DEFS="-DHAVE_CONFIG_H -D_GNU_SOURCE"

[ "$mode" = "static" ] && mv -f bash bash.static || :
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,etc/skel}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/bash $RPM_BUILD_ROOT/bin
%{?_without_static:#}install	bash.static $RPM_BUILD_ROOT/bin

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/bashrc
echo .so bash.1 > $RPM_BUILD_ROOT%{_mandir}/man1/rbash.1

for d in es fr it ja ko nl pl ; do
	install -d $RPM_BUILD_ROOT%{_mandir}/$d/man1
	install man/$d/* $RPM_BUILD_ROOT%{_mandir}/$d/man1
	echo .so bash.1 > $RPM_BUILD_ROOT%{_mandir}/$d/man1/rbash.1
done

ln -sf bash $RPM_BUILD_ROOT/bin/rbash

install %{SOURCE2} $RPM_BUILD_ROOT/etc/skel/.bash_logout
install %{SOURCE3} $RPM_BUILD_ROOT/etc/skel/.bash_profile
install %{SOURCE4} $RPM_BUILD_ROOT/etc/skel/.bashrc

gzip -9nf NEWS README doc/{FAQ,INTRO}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f /etc/shells ]; then
	echo "/bin/bash" > /etc/shells
	echo "/bin/rbash" >> /etc/shells
else
	if ! grep -q '^/bin/bash$' /etc/shells; then
		echo "/bin/bash" >> /etc/shells
	fi
	if ! grep -q '^/bin/rbash$' /etc/shells; then
		echo "/bin/rbash" >> /etc/shells
	fi
fi

[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post static
if [ ! -f /etc/shells ]; then
	echo "/bin/bash.static" > /etc/shells
else
	if ! grep -q '^/bin/bash.static$' /etc/shells; then
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

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz doc/{FAQ,INTRO}.gz

%config %verify(not md5 size mtime) %{_sysconfdir}/bashrc
%config(noreplace,missingok) %verify(not md5 size mtime) /etc/skel/.bash_logout
%config(noreplace,missingok) %verify(not md5 size mtime) /etc/skel/.bash_profile
%config(noreplace,missingok) %verify(not md5 size mtime) /etc/skel/.bashrc

%attr(755,root,root) /bin/bash
%attr(755,root,root) /bin/rbash
%attr(755,root,root) %{_bindir}/bashbug

%{_infodir}/bash.info.gz
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%{?_without_static:#}%files static
%{?_without_static:#}%defattr(644,root,root,755)
%{?_without_static:#}%attr(755,root,root) /bin/bash.static
