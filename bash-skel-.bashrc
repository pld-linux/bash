# .bashrc - file executed when executing bash

if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# return if the shell is not interactive (called from scp, etc)
if [[ $- != *i* ]]; then
	return
fi

# Put your local aliases here
