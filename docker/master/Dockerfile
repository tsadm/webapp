FROM debian:stable
MAINTAINER Jeremías Casteglione <jeremias@tincan.co.uk>

COPY apt.sources /etc/apt/sources.list
COPY apt.preferences /etc/apt/preferences

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get clean && apt-get update -y && apt-get dist-upgrade -y

COPY apt.preferences-django /etc/apt/preferences.d/django
COPY apt.preferences-ansible /etc/apt/preferences.d/ansible

RUN apt-get clean && apt-get update -y \
    && apt-get install -y --no-install-recommends \
        python3-django ansible ssh \
    && apt-get autoremove --purge -y && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*.deb \
        /var/cache/apt/*cache.bin

VOLUME ["/opt/tsadm/webapp", "/opt/tsadm/ansible"]
WORKDIR /opt/tsadm/webapp

ENV TSADM_LOG warning

RUN groupadd tsadm
RUN useradd -c tsadm -m -g tsadm -s /usr/sbin/nologin tsadm

USER tsadm:tsadm
RUN ssh-keygen -b 4096 -t rsa -N '' -f ~/.ssh/id_rsa
