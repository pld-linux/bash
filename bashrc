# /etc/bashrc

# System wide functions and aliases
# Environment stuff goes in /etc/profile

# Test for an interactive shell.  There is no need to set anything
# past this point for scp and rcp, and it's important to refrain from
# outputting anything in those cases.
if [[ $- != *i* ]] ; then
	# Shell is non-interactive.  Be done now!
	return
fi

# If this is an xterm set the title to user@host:dir
case $TERM in
	gnome|nxterm|xterm*|rxvt*)
		PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME}: ${PWD}\007"'
		;;
	*)
		;;
esac
PS1="[\u@\h \W]\\$ "

alias which="type -p"

# SYSTEM WIDE ALIASES ETC.
if [ "$(echo /etc/shrc.d/*.sh)" != "/etc/shrc.d/*.sh" ]; then
	for i in /etc/shrc.d/*.sh; do
		. $i
	done
	unset i
fi
