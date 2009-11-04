# .bash_profile - file executed when logging in

# execute local (and so system wide) rc file only when interactive (not from scp etc.)
# bash is too dumb to do in on it's own when started as login shell
if [[ $- = *i* ]] && [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

export HISTSIZE=1000
export HISTFILESIZE=1000
export TMP=~/tmp
export TMPDIR=$TMP

# setup LOCALE variables
#export LANG=
#export LC_ALL=
#export LANGUAGE=
#export TZ=

# only You can access your files
#umask 077

# turn off accept of 'wall' and 'write':
#[ ! -x /usr/bin/mesg ] || mesg n
