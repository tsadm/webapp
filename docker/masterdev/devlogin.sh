#!/bin/bash
PATH=/usr/sbin:/usr/bin:/sbin:/bin
set -e
groupmod -g ${DOCKER_GID} tsadm
usermod -g ${DOCKER_GID} -u ${DOCKER_UID} tsadm
umask ${DOCKER_UMASK}
set +e
su -s /bin/bash -l tsadm
