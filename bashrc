# /etc/bashrc

# System wide functions and aliases
# Environment stuff goes in /etc/profile

# We set PS1 for each terminal:
case $TERM in
	gnome|xterm*|rxvt)
		PS1="\[\033]0;\u@\h: \w\007\][\u@\h \W]\\$ "
		;;
	*)
		PS1="[\u@\h \W]\\$ "
		;;
esac

alias which="type -p"

# SYSTEM WIDE ALIASES ETC.
if [ "$(echo /etc/shrc.d/*.sh)" != "/etc/shrc.d/*.sh" ]; then
	for i in /etc/shrc.d/*.sh; do
		. $i
	done
	unset i
fi

[ -n "$TERM" ] && tty >/dev/null 2>&1 && stty erase `tput kbs`
