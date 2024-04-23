%define _source_payload w0.gzdio
%define _binary_payload w0.gzdio
%define __jar_repack 0
Name: hello-service
Version: 0.1.0
Release: 1
Summary: Hello Service
License: (c) null
Group: Unspecified
Requires: java >= 11
autoprov: yes
autoreq: yes
BuildArch: noarch
BuildRoot: /shared/rpm-systemd-hw/hello-service/target/rpm/hello-service/buildroot

%description

%install

if [ -d $RPM_BUILD_ROOT ];
then
  mv /shared/rpm-systemd-hw/hello-service/target/rpm/hello-service/tmp-buildroot/* $RPM_BUILD_ROOT
else
  mv /shared/rpm-systemd-hw/hello-service/target/rpm/hello-service/tmp-buildroot $RPM_BUILD_ROOT
fi

%files

%attr(-,vagrant,vagrant)  "/opt/hello//logback.xml"
%attr(-,vagrant,vagrant)  "/opt/hello//stop.sh"
%attr(-,vagrant,vagrant)  "/opt/hello//start.sh"
%attr(-,vagrant,vagrant)  "/opt/hello//com/gvisoc/hello/StopMonitor.class"
%attr(-,vagrant,vagrant)  "/opt/hello//com/gvisoc/hello/task/HelloTask.class"
%attr(-,vagrant,vagrant)  "/opt/hello//com/gvisoc/hello/Stop.class"
%attr(-,vagrant,vagrant)  "/opt/hello//com/gvisoc/hello/StopMonitorMBean.class"
%attr(-,vagrant,vagrant)  "/opt/hello//com/gvisoc/hello/Start.class"
%attr(-,vagrant,vagrant)  "/opt/hello//application.properties"
  "/etc/systemd/system//hello.service"
%dir  "/opt/hello/logs/"

%pre
if [ -f /tmp/hello.pid ]; then
                                echo "Stopping previous service version"
                                systemctl stop hello
                            fi

%post
chmod ugo+x /opt/hello/*.sh
                            echo "Refreshing systemd services"
                            systemctl daemon-reload
                            echo "Starting service"
                            systemctl start hello
                            echo "Enabling boot time start"
                            systemctl enable hello

%preun
if [ -f /tmp/hello.pid ]; then
                                echo "Stopping service before removal"
                                systemctl stop hello
                            fi
