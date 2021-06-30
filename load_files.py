import os
import pandas as pd
sep = os.sep

import datetime

class Clock(object):
    def __init__(self):
        self.reset()
    def reset(self):
        self.accumulator = datetime.timedelta(0)
        self.started = None
    def start_stop(self):
        if self.started:
            self.accumulator += (
                datetime.datetime.utcnow() - self.started
            )
            self.started = None
        else:
            self.started = datetime.datetime.utcnow()
    @property
    def elapsed(self):
        if self.started:
            return self.accumulator + (
                datetime.datetime.utcnow() - self.started
            )
        return self.accumulator
    def __repr__(self):
        return "<Clock {} ({})>".format(
            self.elapsed,
            'started' if self.started else 'stopped'
        )

load_dir = r'C:\Users\Niv\Desktop\hackaton'+sep
watch_dir = load_dir+'watch_cntrl'+sep
sleep_dir = load_dir+'scoring_cntrl'+sep

sleep_list = [fn for fn in os.listdir(sleep_dir) if 'description' not in fn]
watch_list = [fn for fn in os.listdir(watch_dir) if fn.endswith('txt')]


watch_start = [(20, 30), (17, 15), (20, 0), (20, 1), (18, 1), (20, 1), (18, 1), (19, 0), (23, 59), (19, 1), (17, 0), (13, 27), (17, 1), (19, 0)]

for i, sub in enumerate(watch_list):
    curr_sub = pd.read_csv(watch_dir+sub).iloc[:, 0]
    sub_time = pd.DataFrame(columns=['Zero_Crossing_Mode', 'Time'])
    sub_time['Zero_Crossing_Mode'] = curr_sub.values
    start_time = datetime.datetime(1, 1, 1, watch_start[i][0], watch_start[i][1])
    sub_time.at[0, 'Time'] = str(start_time.hour)+':'+str(start_time.minute)
    time_list = []
    for j in range(len(sub_time)):

        time_list.append()



    print('')



print('')
