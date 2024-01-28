class dool_plugin(dool):

    def __init__(self):
        self.name = 'Updates'
        self.type = 's'
        self.width = 5

        self.scale = 0
        self.vars = ('Updates',)

    def extract(self):

        for line in open("/tmp/dool_checkupdates", 'r').readlines():
            l = line.split()
            self.val['Updates'] = int(l[0])
