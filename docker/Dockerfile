FROM ubuntu:latest
RUN apt-get update && \
	apt-get install -y python3 python3-pip python3-flask python3-requests git
WORKDIR /OPENSTACK_K8_SIMPLE_WEB_APP
RUN git clone https://github.com/cj667113/OPENSTACK_K8_SIMPLE_WEB_APP.git .
EXPOSE 80
ENV FLASK_APP=/OPENSTACK_K8_SIMPLE_WEB_APP/flask/openstack_k8_simple_web_app.py
CMD ["flask","run","--host=0.0.0.0","--port=80"]
