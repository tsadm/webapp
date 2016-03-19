FROM debian:stable
MAINTAINER Jeremías Casteglione <jeremias@tincan.co.uk>

COPY apt.sources /etc/apt/sources.list
COPY apt.preferences /etc/apt/preferences

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get clean && apt-get update -y && apt-get dist-upgrade -y

COPY apt.preferences-django /etc/apt/preferences.d/django
COPY apt.preferences-ansible /etc/apt/preferences.d/ansible

RUN apt-get clean && apt-get update -y \
    && apt-get install -y --no-install-recommends python python3 \
        python3-django \
        ansible \
    && apt-get autoremove --purge -y && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*.deb \
        /var/cache/apt/*cache.bin

VOLUME ["/opt/tsadm/webapp"]
WORKDIR /opt/tsadm/webapp

ENV TSADM_LOG warning
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
