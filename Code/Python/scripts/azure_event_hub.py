import sys
import optparse
from proton import *
import urllib


mng = Messenger()
mng.start()

nb_partitions = 8
sasKeyName = "sasKeyName"
sasPolicyKey = "sasKey"
# safeSasPolicyKey = urllib.quote(sasPolicyKey, "")
safeSasPolicyKey = sasPolicyKey

args = []
for i in range(0, nb_partitions):
    address = "amqps://%s:%s@eventhub-namespace.servicebus.windows.net/NAME/ConsumerGroups/$Default" % (
        sasKeyName, safeSasPolicyKey)
    args.append(address + "/Partitions/" + str(i))

print(args)

for a in args:
    # mng.subscribe(a)
    mng.subscribe(a)
    print "Subscribed to %s" % (a)

msg = Message()
while True:
    mng.recv()
    while mng.incoming:
        try:
            mng.get(msg)
        except Exception, e:
            print e
        else:
            print msg.address, msg.subject or "(no subject)", msg.properties, msg.body