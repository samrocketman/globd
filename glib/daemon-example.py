#!/usr/bin/env python

import signal
import sys
import time
from daemon import Daemon

class MyDaemon(Daemon):
    def handler(self, signum = None, frame = None):
        """
        A signal handler for the daemon.
        """
        self.delpid()
        sys.exit(0)
    def run(self):
        for sig in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT]:
            signal.signal(sig, self.handler)
        while True:
            time.sleep(1)

if __name__ == "__main__":
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)

