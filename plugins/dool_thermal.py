class dool_plugin(dool):

    def __init__(self):
        self.name = 'thermal'
        self.type = 's'
        self.width = 4

        self.scale = 0
        self.vars = ('Temp',)

    def extract(self):

        for line in open("/tmp/dool_thermal", 'r').readlines():
            l = line.split()
            self.val['Temp'] = l[0]
