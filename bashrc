# /etc/bashrc

# System wide functions and aliases
# Environment stuff goes in /etc/profile

# If this is an xterm set the title to user@host:dir
case $TERM in
	gnome|nxterm|xterm*|rxvt*)
		PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME}: ${PWD}\007"'
		;;
	*)
		;;
esac

PS1="[\u@\h \W]\\$ "
export PS1

alias which="type -p"

# SYSTEM WIDE ALIASES ETC.
if [ "$(echo /etc/shrc.d/*.sh)" != "/etc/shrc.d/*.sh" ]; then
	for i in /etc/shrc.d/*.sh; do
		. $i
	done
	unset i
fi

[ -n "$TERM" -a "$TERM" != "rxvt" ] && tty >/dev/null 2>&1 && \
	tput kbs >/dev/null 2>&1 && stty erase `tput kbs`
