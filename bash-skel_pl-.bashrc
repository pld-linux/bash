# .bashrc - file executed when executing bash

if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

TEMP=~/tmp
TMPDIR="$TEMP"
export TEMP TMPDIR

LANG=pl_PL
export LANG

umask 077
