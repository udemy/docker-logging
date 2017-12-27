# docker-logging

This repository contains examples of various concepts when logging from containers.

Build the docker container
> docker build -t logging-101:v1 .

## Example 1 ##

Setup:
- docker running on single host
- rsyslog process running on single host

In the example, the application is writing to STDOUT and STDERR.
We can capture the messages logged inside the container to syslog using the Syslog logging driver. 

> docker run --log-driver syslog --log-opt syslog-address=unixgram:///dev/log logging-101:v1 example-1/example_1.py

- we specify the logging driver as Syslog
- we specify the protocol as UDP via `unixgram`
- the socket is `/dev/log`
