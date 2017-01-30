#!/usr/bin/env python2

import os
import sys


class App():

    def run(self):
        variables = ' '.join(['-v %s=%s' % (key.replace('INSTALL_', '').lower(), value)
                              for key, value in os.environ.iteritems()
                              if key.startswith('INSTALL_')])

        print("Executing install script on database '%s'" % sys.argv[1])
        print("Vars: %s" % variables)
        os.system('psql -f install.sql "%s" %s' % (sys.argv[1], variables))


if __name__ == '__main__':
    app = App()
    app.run()
