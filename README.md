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
