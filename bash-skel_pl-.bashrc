# .bashrc - file executed when executing bash

if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

TEMP=~/tmp
TMPDIR="$TEMP"
export TEMP TMPDIR

LANG=pl_PL
LC_ALL=pl
export LANG LC_ALL

umask 077
