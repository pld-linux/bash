# /etc/bashrc

# System wide functions and aliases
# Environment stuff goes in /etc/profile

# For some unknown reason bash refuses to inherit
# PS1 in some circumstances that I can't figure out.
# Putting PS1 here ensures that it gets loaded every time.
#PS1="[\u@\h \W]\\$ "

alias which="type -p"

# SYSTEM WIDE ALIASES ETC.
for i in `find /etc/shrc.d -name '*.sh'` ; do
	. $i
done
unset i

stty erase `tput kbs`
