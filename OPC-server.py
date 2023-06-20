from opcua import Server
from random import randint
import datetime
import time

server = Server()

url = "opc.tcp://192.168.73.128:4840"
server.set_endpoint(url)

name =  "OPCUA_SIMULATION_Server"
addspace =  server.register_namespace(name)

node = server.get_objects_node()

param = node.add_object(addspace, "Parameters")

long = param.add_variable(addspace, "Longitude",0)
lat = param.add_variable(addspace, "Latitude",0)
alt = param.add_variable(addspace, "Altitude",0)
t = param.add_variable(addspace, "Time",0)

long.set_writable()
lat.set_writable()
alt.set_writable()
t.set_writable()

server.start()
print("Server started at {}".format(url))


while True:

    l=randint(-180,180)
    la=randint(-90,90)
    a=randint(0,100)
    ti=datetime.datetime.now()

    long.set_value(l)
    lat.set_value(la)
    alt.set_value(a)
    t.set_value(ti)

    print(l,la,a,ti)

    time.sleep(2)

