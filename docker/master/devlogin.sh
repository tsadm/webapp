#!/bin/bash
PATH=/usr/sbin:/usr/bin:/sbin:/bin
set -e
umask ${DOCKER_UMASK}
groupadd -g ${DOCKER_GID} tsadm
useradd -c tsadm -m -g ${DOCKER_GID} -u ${DOCKER_UID} -s /usr/sbin/nologin tsadm
set +e
exec su -s /bin/bash -l tsadm
