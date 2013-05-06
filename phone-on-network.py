import time
import commands
from datetime import datetime


phones = {
    'ryan': {
        'mac': '98:B8:E3:74',
        'state': 'away',
    },
    'angela': {
        'mac': 'xx:xx:xx:xx',
        'state': 'away',
    }
}

while (True):
    print "Checking..."
    res = commands.getstatusoutput("sudo arp-scan -l --retry=3")
    for name, data in phones.items():
        state = data['state']
        if data['mac'].lower() in res[1].lower():
            if state != "home":
                print "%s came home at %s" % (name, datetime.now())
                phones[name]['state'] = "home"
        else:
            if state != "away":
                print "%s left home at %s" % (name, datetime.now())
                phones[name]['state'] = "away"
    time.sleep(20)
