#!/bin/bash
PATH=/usr/sbin:/sbin:/usr/bin:/bin
set -e
service ssh start
exec bash -l
