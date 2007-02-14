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

# only You can access your files
#umask 077

# turn off accept of 'wall' and 'write':
#[ ! -x /usr/bin/mesg ] || mesg n
