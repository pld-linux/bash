# .bash_profile - file executed when logging in

if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

HISTSIZE=1000
HISTFILESIZE=1000

export HISTSIZE HISTFILESIZE

mesg n
