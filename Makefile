RSYNC		= -e ssh -azv --cvs-exclude --delete

HOST		= root@factorio.lescigales.org
DIR		= /var/tmp/httpd-protect
REMOTE_DEVEL	= $(HOST):$(DIR)

.PHONY	: httpd

default: httpd
httpd:
	@clean
	@rsync $(RSYNC) . $(REMOTE_DEVEL)
