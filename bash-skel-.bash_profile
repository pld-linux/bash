# .bash_profile - file executed when logging in

if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

HISTSIZE=1000
HISTFILESIZE=1000

export HISTSIZE HISTFILESIZE

mesg n

TMP=~/tmp
TMPDIR="$TMP"
export TMP TMPDIR

# setup LOCALE variables
#LANG=
#LC_ALL=
#export LANG LC_ALL

umask 077

