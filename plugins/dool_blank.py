### Author: Custom

class dool_plugin(dool):

    def __init__(self):
        self.name = 'blank'
        self.nick = ( 'f' )
        self.vars = ( 'f' )
        self.type = 's'
        self.width = 2
        self.scale = 0

    def extract(self):
        self.val = { 'f':'||' }

# vim:ts=4:sw=4:et
