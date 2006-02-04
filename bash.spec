#
# Conditional build:
%bcond_without	static		# don't build static version
%bcond_with	bash_history	# build with additional history in /var/log/bash_hist ;)
##
%define		_ver		3.1
%define		_patchlevel	007
%define		_rel		1
#
Summary:	GNU Bourne Again Shell (bash)
Summary(fr):	Le shell Bourne Again de GNU
Summary(pl):	Pow³oka GNU Bourne Again Shell (bash)
Name:		bash
Version:	%{_ver}.%{_patchlevel}
Release:	%{_rel}%{?with_bash_history:inv}
License:	GPL
Group:		Applications/Shells
Source0:	ftp://ftp.gnu.org/pub/gnu/bash/%{name}-%{_ver}.tar.gz
# Source0-md5:	ef5304c4b22aaa5088972c792ed45d72
Source1:	%{name}rc
Source2:	%{name}-skel-.%{name}_logout
Source3:	%{name}-skel-.%{name}_profile
Source4:	%{name}-skel-.%{name}rc
Source5:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source5-md5:	d2aacf89c4a444c5da648da69afdb01a
Patch0:		%{name}-paths.patch
Patch1:		%{name}-security.patch
Patch2:		%{name}-autoconf.patch
Patch3:		%{name}-info.patch
Patch4:		%{name}-profile.patch
Patch5:		%{name}-requires.patch
Patch6:		%{name}-compat.patch
Patch8:		%{name}-sighup.patch
Patch9:		%{name}-backup_history.patch
Patch10:	%{name}-pmake.patch
Patch11:	%{name}-act_like_sh.patch
Patch101:	ftp://ftp.cwru.edu/pub/bash/bash-3.1-patches/bash31-001
Patch102:	ftp://ftp.cwru.edu/pub/bash/bash-3.1-patches/bash31-002
Patch103:	ftp://ftp.cwru.edu/pub/bash/bash-3.1-patches/bash31-003
Patch104:	ftp://ftp.cwru.edu/pub/bash/bash-3.1-patches/bash31-004
Patch105:	ftp://ftp.cwru.edu/pub/bash/bash-3.1-patches/bash31-005
Patch106:	ftp://ftp.cwru.edu/pub/bash/bash-3.1-patches/bash31-006
Patch107:	ftp://ftp.cwru.edu/pub/bash/bash-3.1-patches/bash31-007
URL:		http://www.gnu.org/software/bash/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 5.1
BuildRequires:	texinfo
%if %{with static}
# Require static library only for static build
BuildRequires:	glibc-static >= 2.2
BuildRequires:	ncurses-static >= 5.2
BuildRequires:	readline-static >= 5.1
%endif
Requires(post,preun):	grep
Requires(preun):	fileutils
Requires:	grep
Requires:	readline >= 5.1
Requires:	setup >= 2.4.6-2
Obsoletes:	bash-doc
Obsoletes:	bash2
Obsoletes:	bash2-doc
Obsoletes:	etcskel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l es
Bash es un interpretador de comandos compatible con sh, que ejecuta
comandos leídos de la entrada padrón o de un archivo. Bash también
incorpora características útiles de las shells Korn y C (ksh y csh).
Bash ha sido desarrollado para ser una adición compatible con la
especificación IEEE Posix para shells y herramientas (IEEE Working
Group 1003.2).

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
stosunku do sh, w³±czaj±c edycjê linii poleceñ, nieograniczony rozmiar
historii poleceñ, funkcje i aliasy, indeksowane tablice
nieograniczonych rozmiarów oraz arytmetykê ca³kowitoliczbow± o
dowolnej podstawie od 2 do 64. W zamierzeniu ostatecznie ma byæ zgodny
ze standardem IEEE POSIX P1003.2/ISO 9945.2 Shell and Tools.

%description -l pt_BR
Bash é um interpretador de comandos compatível com sh, que executa
comandos lidos da entrada padrão ou de um arquivo. Bash também
incorpora características úteis das shells Korn e C (ksh e csh). Bash
tem sido desenvolvido para ser uma implementação compatível com a
especificação IEEE Posix para shells e ferramentas (IEEE Working Group
1003.2).

%description -l ru
Bash - ÜÔÏ sh-ÓÏ×ÍÅÓÔÉÍÙÊ ÉÎÔÅÒÐÒÅÔÁÔÏÒ ËÏÍÁÎÄÎÏÇÏ ÑÚÙËÁ (shell),
ÉÓÐÏÌÎÑÀÝÉÊ ËÏÍÁÎÄÙ, ÐÏÓÔÕÐÁÀÝÉÅ ÓÏ ÓÔÁÎÄÁÒÔÎÏÇÏ ××ÏÄÁ ÉÌÉ ÉÚ ÆÁÊÌÁ.
Bash ×ËÌÀÞÁÅÔ ÐÏÌÅÚÎÙÅ ÒÁÓÛÉÒÅÎÉÑ ÉÚ ÉÎÔÅÒÐÒÅÔÁÔÏÒÏ× Korn É C shell
(ksh É csh).

Bash ÒÁÚÒÁÂÁÔÙ×ÁÅÔÓÑ ËÁË ÒÅÁÌÉÚÁÃÉÑ, ÏÔ×ÅÞÁÀÝÁÑ IEEE Posix Shell and
Tools specification (IEEE Working Group 1003.2).

%description -l tr
Bash standart giriþten ya da bir dosyadan komut okuyup çalýþtýran sh
uyumlu bir komut dili yorumlayýcýsýdýr. Ayný zamanda Korn ve C
kabuklarýnýn (ksh ve csh) kullanýþlý özelliklerini de kapsar. Bash,
IEEE Posix Kabuk ve Araç ayrýntýlarýna (IEEE Working Group 1003.2)
uyumlu bir uygulama olarak tasarlanmýþtýr.

%description -l uk
Bash - ÃÅ sh-ÓÕÍ¦ÓÔÎÉÊ ¦ÎÔÅÒÐÒÅÔÁÔÏÒ ËÏÍÁÎÄÎÏ§ ÍÏ×É (shell),
×ÉËÏÎÕÀÞÉÊ ËÏÍÁÎÄÉ Ú¦ ÓÔÁÎÄÁÒÔÎÏÇÏ ××ÏÄÕ ÁÂÏ Ú ÆÁÊÌÁ. Bash Í¦ÓÔÉÔØ
ËÏÒÉÓÔÎ¦ ÒÏÚÛÉÒÅÎÎÑ Ú ¦ÎÔÅÒÐÒÅÔÁÔÏÒ¦× Korn ÔÁ C shell (ksh ÔÁ csh).

Bash ÒÏÚÒÏÂÌÑ×ÓÑ ÑË ÒÅÁÌ¦ÚÁÃ¦Ñ, ÝÏ ×¦ÄÐÏ×¦ÄÁ¤ IEEE Posix Shell and
Tools specification (IEEE Working Group 1003.2).

%package static
Summary:	Statically linked GNU Bourne Again Shell (bash)
Summary(pl):	Statycznie skonsolidowany GNU Bourne Again Shell (bash)
Group:		Applications/Shells
Requires(post,preun):	grep
Requires(preun):	fileutils
Requires:	%{name} = %{version}-%{release}

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
You'll probably end up using it. This package contains statically
linked version of bash.

%description static -l pl
Bash jest zaawansowan± pow³ok±, która wykonuje komendy czytane ze
standardowego wej¶cia (stdin) lub z pliku. Posiada w³a¶ciwo¶ci pow³ok
Korn i C (ksh i csh). Bash jest równie¿ zaimplementowany IEEE Posix
Shell oraz jest zgodny ze specyfikacj± - IEEE Working Group 1003.2. W
tym pakiecie jest wersja basha skonsolidowana statycznie.

%prep
%setup -q -n %{name}-%{_ver} -a5
# official patches
%patch101 -p0
%patch102 -p0
%patch103 -p0
%patch104 -p0
%patch105 -p0
%patch106 -p0
%patch107 -p0

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch8 -p1
%{?with_bash_history:%patch9 -p1}
#%patch10 -p1	-- no longer needed?
%patch11 -p1

%build
%{__autoconf}
cp -f /usr/share/automake/config.* support
for mode in %{?with_static:static} shared; do
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
	--enable-separate-helpfiles \
	--without-bash-malloc \
	`[ "$mode" = "static" ] && echo "--enable-static-link"` \
	--with-installed-readline

%{__make} \
	DEFS="-DHAVE_CONFIG_H -D_GNU_SOURCE"

[ "$mode" = "static" ] && mv -f bash bash.static || :
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/bin,/etc/skel,%{_datadir}/%{name}}
%{?with_bash_history:install -d $RPM_BUILD_ROOT/var/log/bash_hist}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/bash $RPM_BUILD_ROOT/bin
%{?with_static:install bash.static $RPM_BUILD_ROOT/bin}

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
rm -f $RPM_BUILD_ROOT/usr/share/info/dir

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
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

%preun
if [ "$1" = "0" ]; then
	umask 022
	grep -v /bin/bash /etc/shells | grep -v /bin/rbash > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%post static
umask 022
if [ ! -f /etc/shells ]; then
	echo "/bin/bash.static" > /etc/shells
else
	if ! grep -q '^/bin/bash.static$' /etc/shells; then
		echo "/bin/bash.static" >> /etc/shells
	fi
fi

%preun static
if [ "$1" = "0" ]; then
	umask 022
	grep -v /bin/bash.static /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES NEWS README doc/{FAQ,INTRO}

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bashrc
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/skel/.bash_logout
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/skel/.bash_profile
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/skel/.bashrc

%attr(755,root,root) /bin/bash
%attr(755,root,root) /bin/rbash
%attr(755,root,root) %{_bindir}/bashbug

%{?with_bash_history:%attr(751,root,root) %dir /var/log/bash_hist}
%{_infodir}/bash.info*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_datadir}/%{name}

%if %{with static}
%files static
%defattr(644,root,root,755)
%attr(755,root,root) /bin/bash.static
%endif
