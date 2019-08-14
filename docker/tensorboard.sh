#!/bin/bash

docker logs -f --timestamps $(docker run --rm -d -e PYTHONIOENCODING=utf-8 --name="comment_tb" \
-v `pwd`/source:/source \
-p 7001:6006 \
ductricse/dl-gpu /bin/bash -c "/source/scripts/tensorboard.sh")
