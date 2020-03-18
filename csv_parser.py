macs = []

with open('connected_ports.csv', 'r') as csv:
    for line in csv:
        # get raw with mac in csv
        mac = line.split(';')[0]
        macs.append(mac)

macs = set(macs)

with open('mac.txt', 'w') as f:
    for mac in macs:
        f.write(mac)
