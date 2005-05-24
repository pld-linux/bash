# /etc/bashrc

# System wide functions and aliases
# Environment stuff goes in /etc/profile

# For some unknown reason bash refuses to inherit
# PS1 in some circumstances that I can't figure out.
# Putting PS1 here ensures that it gets loaded every time.
#PS1="[\u@\h \W]\\$ "

alias which="type -p"

# SYSTEM WIDE ALIASES ETC.
# use shell glob to get files sorted and prevent extra dep on findutils
if [ "$(echo /etc/shrc.d/*.sh)" != "/etc/shrc.d/*.sh" ]; then
	for i in /etc/shrc.d/*.sh; do
		. $i
	done
	unset i
fi
