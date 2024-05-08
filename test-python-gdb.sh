#!/usr/bin/env bash
gdb \
    -ex 'rbreak src/python/grpcio/grpc/_cython' \
    -ex 'break cq_next' \
    -ex 'rbreak cygrpc' \
    -ex 'run' \
    --args python3 grpc_segfault.py
