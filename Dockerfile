FROM python:3.10.5-slim-buster

MAINTAINER Javier Matilla Martín
RUN apt update
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y apache2 libapache2-mod-wsgi-py3 && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY requirements.txt ./
#enable mod_wsgi
RUN a2dissite 000-default.conf
RUN a2dissite default-ssl.conf
RUN a2enmod wsgi

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

COPY ./ /var/www/src

#Creamos el virtual host
COPY apache/flask.conf /etc/apache2/sites-available/flask.conf
RUN chown -R www-data:www-data /var/www/src
RUN chown www-data:www-data /etc/apache2/sites-available/flask.conf
RUN a2ensite flask.conf

#RUN chown -R www-data:www-data /usr/local/lib/python3.10
RUN umask 022
RUN pip3 install -r requirements.txt
EXPOSE 80

#CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
