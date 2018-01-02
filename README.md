# docker-logging

This repository contains examples of various concepts when logging from containers.

Build the docker container
> docker build -t logging-101:v1 .

## Example 1 ##

In the example, the application is writing to STDOUT and STDERR.
We can capture the messages logged inside the container to syslog running on the host machine using the Syslog logging driver. 

Setup:
- docker running on single linux host
- rsyslog is also running on the host

> docker run --log-driver syslog --log-opt syslog-address=unixgram:///dev/log logging-101:v1 example-1/example_1.py

- specify the logging driver as Syslog
- specify the protocol as UDP via `unixgram`
- the socket is `/dev/log`


## Example 2 ##

In this example, the application is logging to the Unix syslog using the Python SysLogHandler.
It is sending to the domain socket `/dev/log`. By default, the path does not exists inside the container. We will mount the path on the host machine to the container to allow the host machine to capture the messages.

Setup:
- docker running on single linux host
- rsyslog running on the host

> docker run --mount type=bind,source=/dev/log,target=/dev/log logging-101:v1 example-2/example_2.py

- this expose the `/dev/log` address to the container
- I used the bind mount option instead of a volume because the address is not maintained by docker


## Example 3 ##

In this example, the application is logging to STDOUT and STDERR.
Instead of relying on the host machine to provide the rsyslog service, we can created a dedicated logging container. 
The logging container will expose the listening port and log data to a location that is mounted on the host.

Setup:
- docker running on the single linux host
- rsyslog container running on the host

> docker run -d --mount type=bind,source=/tmp/clogs,target=/var/log -p 127.0.0.1:5514:514/udp  --name rsyslog voxxit/rsyslog

- `/tmp/clogs` is a directory on the local host. It is mounted on the container as `/var/log`. Rsyslog writes data to `/var/log/messages`
- the container listens on port 5514 of the local host and routes to port 514 on internal network

> docker run --log-driver syslog --log-opt syslog-address=udp://127.0.0.1:5514 --log-opt syslog-facility=daemon --log-opt tag=app101 --name=logging-ex3 logging-101:v1 example-1/example_1.py

- specify the logging driver as Syslog
- specify the networking address of the Rsyslog process

You can run multiple instances of the application and all of them will log to the same rsyslog container. Tail the log to see all the messages.


## Example 4 ##

In this example, the application is logging to Unix syslog just like in Example 2.
We will also created a dedicated logging container that will run Rsyslog. We will make use of a volume share the `/dev/log` socket address between containers. A volume makes sense in this case becase it is only intended to be visible to docker containers.

Setup:
- docker running on the single linux host
- rsyslog container running on the host





