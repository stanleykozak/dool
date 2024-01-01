### Authority: Dag Wieers <dag@wieers.com>

class dool_plugin(dool):
    """
    Most expensive CPU process.

    Displays the process that uses the CPU the most during the monitored
    interval. The value displayed is the percentage of CPU time for the total
    amount of CPU processing power. Based on per process CPU information.
    """
    def __init__(self):
        self.name = 'cpu custom'
        self.vars = ('process|pid|cpu_usage',)
        self.type = 's'
        self.width = 34
        self.scale = 0
        self.pidset1 = {}

    def extract(self):
        self.output = ''
        self.pidset2 = {}
        self.val['max'] = 0.0
        for pid in proc_pidlist():
            try:
                ### Using dopen() will cause too many open files
                l = proc_splitline('/proc/%s/stat' % pid)
            except IOError:
                continue

            if len(l) < 20: continue

            ### Reset previous value if it doesn't exist
            if pid not in self.pidset1:
                self.pidset1[pid] = 0

            self.pidset2[pid] = int(l[13]) + int(l[14])
            usage = (self.pidset2[pid] - self.pidset1[pid]) * 1.0 / elapsed / cpunr

            ### Is it a new topper ?
            if usage < self.val['max']: continue

            # name = l[1][1:-1]

            self.val['max'] = usage
            self.val['pid'] = pid
            self.val['name'] = getnamebypid(pid, proc_splitline('/proc/%s/stat' % pid)[1])

        if self.val['max'] != 0.0:
            self.output = '%-20.20s %7s %05.1f' % (self.val['name'], self.val['pid'], self.val['max'])
            

        ### Debug (show PID)
             # self.output = '%-*s%s%s' % (self.width, self.val['pid'], self.width-6, self.val['name'], cprint(self.val['max'], 'f', 3, 34))

        if step == op.delay:
            self.pidset1 = self.pidset2

    def showcsv(self):
        # return '%s|%d%%' % (self.val['name'], self.val['max'])
        return '%s,%s,%s' % (self.val['name'], self.val['pid'], self.val['max'])
# vim:ts=4:sw=4:et
