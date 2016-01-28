FROM django:latest
MAINTAINER Jeremías Casteglione <jeremias@tincan.co.uk>
VOLUME ["/opt/tsadm/django"]
WORKDIR /opt/tsadm/django
EXPOSE 8000
USER 65534:65534
CMD ["/opt/tsadm/django/manage.py", "runserver", "0.0.0.0:8000"]
