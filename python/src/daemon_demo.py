import daemon


class App(object):
    pass


import time
from datetime import datetime
from daemon import runner


def run():
    while True:
        print(f"{datetime.now()}")
        time.sleep(1)
    pass


with daemon.DaemonContext():
    run()
    pass

app = App()

daemon_runner = runner.DaemonRunner(app)

daemon_runner.do_action()
