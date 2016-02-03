FROM django:latest
MAINTAINER Jeremías Casteglione <jeremias@tincan.co.uk>
VOLUME ["/opt/tsadm/webapp"]
WORKDIR /opt/tsadm/webapp
EXPOSE 8000
USER 65534:65534
CMD ["/opt/tsadm/webapp/manage.py", "runserver", "0.0.0.0:8000"]
