class dool_plugin(dool):

    def __init__(self):
        self.name = 'systemd'
        self.type = 's'
        self.width = 7

        self.scale = 0
        self.vars = ('Fail','Total','State')

    def extract(self):

        for line in open("/tmp/dool_systemd", 'r').readlines():
            l = line.split()
            self.val['Fail'] =  l[0]
            self.val['Total'] = l[1]
            self.val['State'] = l[2]

