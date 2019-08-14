#!/bin/bash

docker logs -f --timestamps $(docker run --runtime=nvidia -d -e PYTHONIOENCODING=utf-8 --name=comment --rm \
-v `pwd`/source/:/source \
-p 7000:7000 \
ductricse/pytorch /bin/bash -c "jupyter notebook --port=7000 --allow-root --ip=0.0.0.0")

