# .bash_logout - file executed when logging out

if [ -x /sbin/consoletype ] && [ `/sbin/consoletype` = vt ]; then
	clear
fi
