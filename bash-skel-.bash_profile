# .bash_profile - file executed when logging in

if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

export HISTSIZE=1000
export HISTFILESIZE=1000
export TMP=~/tmp
export TMPDIR="$TMP"

# setup LOCALE variables
#export LANG=
#export LC_ALL=

umask 077

if [ -x /usr/bin/mesg ]; then
	mesg n
fi
