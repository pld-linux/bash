# .bashrc - file executed when executing bash

if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

TEMP=~/tmp
TMPDIR="$TEMP"
export TEMP TMPDIR

# setup LOCALE variables
#LANG=
#LC_ALL=
#export LANG LC_ALL


umask 077
