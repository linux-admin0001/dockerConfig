#!/bin/bash

# Interactive run:
# docker run -it --name pybot --hostname debian -- michael/pybot:v1 bash
# Run in background mode:
docker run -it -d --name pybot --hostname debian -p 2222:22 michael/pybot:v1 bash -c "service ssh restart; bash"
#                                              (host):(docker)
