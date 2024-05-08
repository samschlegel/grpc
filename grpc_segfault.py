import gevent.monkey
gevent.monkey.patch_all()

import grpc.experimental.gevent as grpc_gevent
grpc_gevent.init_gevent()

import sys
sys.path.append("examples/python/helloworld")

import examples.python.helloworld.greeter_server as greeter_server
import examples.python.helloworld.greeter_client as greeter_client

greeter_server.serve()
