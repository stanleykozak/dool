### Author: Dag Wieers <dag@wieers.com>

class dool_plugin(dool):

    def __init__(self):
        self.name = 'uptime'
        self.type = 's'
        self.width = 8

        self.scale = 0
        self.vars = ('time',)

    def extract(self):
        for line in open('/proc/uptime', 'r').readlines():
            l = line.split()
            self.val['time'] = l[0]
