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
export PS1

alias which="type -p"

# SYSTEM WIDE ALIASES ETC.
for i in `find /etc/shrc.d -name '*.sh'` ; do
	. $i
done
unset i

stty erase `tput kbs`
