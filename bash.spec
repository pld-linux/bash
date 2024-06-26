# NOTE: when updating patchlevel, do not forget to update 'sources' file:
# $ md5sum bash44-??? > sources
#
# Conditional build:
%bcond_without	static		# static version
%bcond_with	bash_history	# additional history in /var/log/bash_hist ;)
%bcond_without	tests		# unit testing

%define		ver		5.2
%define		patchlevel	26
%define		rel		1
%define		min_readline	8.2
Summary:	GNU Bourne Again Shell (bash)
Summary(fr.UTF-8):	Le shell Bourne Again de GNU
Summary(pl.UTF-8):	Powłoka GNU Bourne Again Shell (bash)
Name:		bash
Version:	%{ver}%{?patchlevel:.%{patchlevel}}
Release:	%{rel}%{?with_bash_history:inv}
License:	GPL v3+
Group:		Applications/Shells
Source0:	https://ftp.gnu.org/gnu/bash/%{name}-%{ver}.tar.gz
# Source0-md5:	cfb4cf795fc239667f187b3d6b3d396f
Source1:	%{name}rc
Source2:	%{name}-skel-.bash_logout
Source3:	%{name}-skel-.bash_profile
Source4:	%{name}-skel-.bashrc
Source5:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source5-md5:	d2aacf89c4a444c5da648da69afdb01a
Patch0:		%{name}-paths.patch
Patch1:		%{name}-security.patch
Patch2:		%{name}-autoconf.patch
Patch3:		%{name}-info.patch
Patch4:		%{name}-profile.patch
Patch5:		%{name}-requires.patch
Patch6:		%{name}-compat.patch
Patch7:		%{name}-loadables.patch
Patch8:		%{name}-sighup.patch
Patch9:		%{name}-backup_history.patch
Patch10:	%{name}-act_like_sh.patch
Patch11:	%{name}-elinks_cont.patch
%patchset_source -f https://ftp.gnu.org/gnu/bash/bash-5.2-patches/bash52-%03g 1 %{patchlevel}
URL:		http://www.gnu.org/software/bash/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= %{min_readline}
BuildRequires:	rpmbuild(macros) >= 1.462
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo
%if %{with static}
# Require static library only for static build
BuildRequires:	glibc-static >= 2.2
BuildRequires:	ncurses-static >= 5.2
BuildRequires:	readline-static >= %{min_readline}
%endif
Requires:	readline >= %{min_readline}
Requires:	setup >= 2.4.6-2
Obsoletes:	bash-doc
Obsoletes:	bash2 < 3
Obsoletes:	bash2-doc < 3
Obsoletes:	etcskel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/%{name}

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

%description -l es.UTF-8
Bash es un interpretador de comandos compatible con sh, que ejecuta
comandos leídos de la entrada padrón o de un archivo. Bash también
incorpora características útiles de las shells Korn y C (ksh y csh).
Bash ha sido desarrollado para ser una adición compatible con la
especificación IEEE Posix para shells y herramientas (IEEE Working
Group 1003.2).

%description -l de.UTF-8
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

%description -l fr.UTF-8
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

%description -l pl.UTF-8
Bash (Bourne Again SHell) jest projektem GNU powłoki kompatybilnej z
sh oraz interpretera języka poleceń. Posiada użyteczne właściwości
powłok Korn (ksh) i C (csh). Większość skryptów sh może być
uruchamiana w bashu bez modyfikacji. Oferuje on kilka ulepszeń w
stosunku do sh, włączając edycję linii poleceń, nieograniczony rozmiar
historii poleceń, funkcje i aliasy, indeksowane tablice
nieograniczonych rozmiarów oraz arytmetykę całkowitoliczbową o
dowolnej podstawie od 2 do 64. W zamierzeniu ostatecznie ma być zgodny
ze standardem IEEE POSIX P1003.2/ISO 9945.2 Shell and Tools.

%description -l pt_BR.UTF-8
Bash é um interpretador de comandos compatível com sh, que executa
comandos lidos da entrada padrão ou de um arquivo. Bash também
incorpora características úteis das shells Korn e C (ksh e csh). Bash
tem sido desenvolvido para ser uma implementação compatível com a
especificação IEEE Posix para shells e ferramentas (IEEE Working Group
1003.2).

%description -l ru.UTF-8
Bash - это sh-совместимый интерпретатор командного языка (shell),
исполняющий команды, поступающие со стандартного ввода или из файла.
Bash включает полезные расширения из интерпретаторов Korn и C shell
(ksh и csh).

Bash разрабатывается как реализация, отвечающая IEEE Posix Shell and
Tools specification (IEEE Working Group 1003.2).

%description -l tr.UTF-8
Bash standart girişten ya da bir dosyadan komut okuyup çalıştıran sh
uyumlu bir komut dili yorumlayıcısıdır. Aynı zamanda Korn ve C
kabuklarının (ksh ve csh) kullanışlı özelliklerini de kapsar. Bash,
IEEE Posix Kabuk ve Araç ayrıntılarına (IEEE Working Group 1003.2)
uyumlu bir uygulama olarak tasarlanmıştır.

%description -l uk.UTF-8
Bash - це sh-сумістний інтерпретатор командної мови (shell),
виконуючий команди зі стандартного вводу або з файла. Bash містить
користні розширення з інтерпретаторів Korn та C shell (ksh та csh).

Bash розроблявся як реалізація, що відповідає IEEE Posix Shell and
Tools specification (IEEE Working Group 1003.2).

%package static
Summary:	Statically linked GNU Bourne Again Shell (bash)
Summary(pl.UTF-8):	Statycznie skonsolidowany GNU Bourne Again Shell (bash)
Group:		Applications/Shells
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

%description static -l pl.UTF-8
Bash jest zaawansowaną powłoką, która wykonuje komendy czytane ze
standardowego wejścia (stdin) lub z pliku. Posiada właściwości powłok
Korn i C (ksh i csh). Bash jest również zaimplementowany IEEE Posix
Shell oraz jest zgodny ze specyfikacją - IEEE Working Group 1003.2. W
tym pakiecie jest wersja basha skonsolidowana statycznie.

%package devel
Summary:	Header files for bash plugins development
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia wtyczek basha
Group:		Development/Libraries
# doesn't require base

%description devel
Header files for bash plugins development.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek basha.

%prep
%setup -q -n %{name}-%{ver} -a5
# official patches
%{?patchlevel:%patchset_patch 1 %{patchlevel}}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%{?with_bash_history:%patch9 -p1}
%patch10 -p1
%patch11 -p1

%{__sed} -i -e 's#/usr/bin/printf#/bin/printf#g' tests/intl2.sub

%build
cp -f /usr/share/automake/config.* support
%{__autoconf}
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
	$([ "$mode" = "static" ] && echo "--enable-static-link") \
	--with-installed-readline

%{__make} \
	DEFS="-DHAVE_CONFIG_H -D_GNU_SOURCE"

if [ "$mode" = "static" ]; then
	%{__mv} bash bash.static
fi
done

%{?with_tests:%{__make} tests}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/bin,/etc/skel,%{_datadir}/%{name}}
%{?with_bash_history:install -d $RPM_BUILD_ROOT/var/log/bash_hist}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_bindir}/bash $RPM_BUILD_ROOT/bin
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

# use our bugtracker, upstream will ignore reports from this anyway
%{__rm} $RPM_BUILD_ROOT%{_bindir}/bashbug \
	$RPM_BUILD_ROOT%{_mandir}/man1/bashbug.1 \
	$RPM_BUILD_ROOT%{_mandir}/*/man1/bashbug.1
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/bash

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p <lua>
%lua_add_etc_shells /bin/bash /bin/rbash
os.execute("/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1")

%preun	-p <lua>
if arg[2] == 0 then
	%lua_remove_etc_shells /bin/bash /bin/rbash
end

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post static -p <lua>
%lua_add_etc_shells /bin/bash.static

%preun static -p <lua>
if arg[2] == 0 then
	%lua_remove_etc_shells /bin/bash.static
end

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGES COMPAT NEWS POSIX README RBASH doc/{FAQ,INTRO,bash.html,bashref.html} 

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bashrc
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/skel/.bash_logout
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/skel/.bash_profile
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/skel/.bashrc

%attr(755,root,root) /bin/bash
%attr(755,root,root) /bin/rbash

%{?with_bash_history:%attr(1733,root,root) %dir /var/log/bash_hist}
%{_infodir}/bash.info*
%{_mandir}/man1/bash.1*
%{_mandir}/man1/rbash.1*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%dir %{_datadir}/%{name}
%doc %{_datadir}/%{name}/*

# loadables
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/accept
%attr(755,root,root) %{_libdir}/%{name}/basename
%attr(755,root,root) %{_libdir}/%{name}/csv
%attr(755,root,root) %{_libdir}/%{name}/cut
%attr(755,root,root) %{_libdir}/%{name}/dirname
%attr(755,root,root) %{_libdir}/%{name}/dsv
%attr(755,root,root) %{_libdir}/%{name}/fdflags
%attr(755,root,root) %{_libdir}/%{name}/finfo
%attr(755,root,root) %{_libdir}/%{name}/getconf
%attr(755,root,root) %{_libdir}/%{name}/head
%attr(755,root,root) %{_libdir}/%{name}/id
%attr(755,root,root) %{_libdir}/%{name}/ln
%attr(755,root,root) %{_libdir}/%{name}/logname
%attr(755,root,root) %{_libdir}/%{name}/mkdir
%attr(755,root,root) %{_libdir}/%{name}/mkfifo
%attr(755,root,root) %{_libdir}/%{name}/mktemp
%attr(755,root,root) %{_libdir}/%{name}/mypid
%attr(755,root,root) %{_libdir}/%{name}/pathchk
%attr(755,root,root) %{_libdir}/%{name}/print
%attr(755,root,root) %{_libdir}/%{name}/printenv
%attr(755,root,root) %{_libdir}/%{name}/push
%attr(755,root,root) %{_libdir}/%{name}/realpath
%attr(755,root,root) %{_libdir}/%{name}/rm
%attr(755,root,root) %{_libdir}/%{name}/rmdir
%attr(755,root,root) %{_libdir}/%{name}/seq
%attr(755,root,root) %{_libdir}/%{name}/setpgid
%attr(755,root,root) %{_libdir}/%{name}/sleep
%attr(755,root,root) %{_libdir}/%{name}/stat
%attr(755,root,root) %{_libdir}/%{name}/strftime
%attr(755,root,root) %{_libdir}/%{name}/sync
%attr(755,root,root) %{_libdir}/%{name}/tee
%attr(755,root,root) %{_libdir}/%{name}/truefalse
%attr(755,root,root) %{_libdir}/%{name}/tty
%attr(755,root,root) %{_libdir}/%{name}/uname
%attr(755,root,root) %{_libdir}/%{name}/unlink
%attr(755,root,root) %{_libdir}/%{name}/whoami

%if %{with static}
%files static
%defattr(644,root,root,755)
%attr(755,root,root) /bin/bash.static
%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/bash
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/Makefile.inc
%{_libdir}/%{name}/Makefile.sample
%{_libdir}/%{name}/loadables.h
%{_pkgconfigdir}/bash.pc
