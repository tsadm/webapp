FROM tsadm/master
MAINTAINER Jeremías Casteglione <jeremias@tincan.co.uk>

USER root:root

COPY apt.preferences-sphinx /etc/apt/preferences.d/sphinx

RUN apt-get clean && apt-get update -y \
    && apt-get install -y --no-install-recommends \
        make python3-coverage python3-sphinx sudo \
    && apt-get autoremove --purge -y && apt-get clean

ENV TSADM_LOG debug

COPY devlogin.sh /root/
COPY sudoers /etc/sudoers.d/tsadm
RUN chmod 0440 /etc/sudoers.d/tsadm

EXPOSE 8000
CMD ["make", "-C src", "django-runserver"]
