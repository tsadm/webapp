FROM debian:stable
MAINTAINER Jeremías Casteglione <jeremias@tincan.co.uk>

COPY apt.sources /etc/apt/sources.list

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get clean && apt-get update -y && apt-get dist-upgrade -y

RUN apt-get clean && apt-get update -y \
    && apt-get install -y --no-install-recommends \
        python \
        ssh \
    && apt-get autoremove --purge -y && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*.deb \
        /var/cache/apt/*cache.bin

RUN groupadd tsadm
RUN useradd -c tsadm -m -g tsadm -s /usr/sbin/nologin tsadm

EXPOSE 22
COPY slave-init.sh /root/

USER tsadm:tsadm
RUN ssh-keygen -b 4096 -t rsa -N '' -f ~/.ssh/id_rsa

USER root:root
CMD ["/root/slave-init.sh"]
