# .bash_profile - file executed when logging in

if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

HISTSIZE=1000
HISTFILESIZE=1000
TMP=~/tmp
TMPDIR="$TMP"

# setup LOCALE variables
#LANG=
#LC_ALL=
#export LANG LC_ALL

export HISTSIZE HISTFILESIZE TMP TMPDIR

umask 077

mesg n
