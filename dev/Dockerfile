FROM centos:7

ENV SENSU_VERSION "1.0.0-1"

RUN yum update -y \
 && yum install -y "epel-release" \
 && yum install -y \
    wget \
    nagios-plugins-all

RUN wget https://sensu.global.ssl.fastly.net/yum/7/x86_64/sensu-$SENSU_VERSION.el7.x86_64.rpm \
 && rpm -ivh sensu-$SENSU_VERSION.el7.x86_64.rpm

ENV PATH $PATH:/opt/sensu/bin

RUN chown -R sensu:sensu /etc/sensu
USER sensu:sensu
WORKDIR /etc/sensu

CMD echo "Set /opt/sensu/bin/<binary> in docker-compose"
