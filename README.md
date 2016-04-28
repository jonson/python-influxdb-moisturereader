# Python Serial influxdb moisture sensor reader

This is a simple example of how to read serial data in python and write it to an influxdb.  IPs and influx db are my local setup, change them to match your environment.

This is meant to be run on a rasbperry pi (I've wired an arduino to talk to my raspberry pi via a serial connection).

## Upstart

I prefer upstart to the system v based scripts, so a quick config file for upstart is in the upstart directory.  This will ensure the process is running (and respawned if needed).  By default upstart is not installed on Raspbian, but can be installed with:

```sh
sudo apt-get install upstart
```
