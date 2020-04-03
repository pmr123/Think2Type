from pyedflib import highlevel
import numpy as np 
from pprint import pprint as print
import os
# # write an edf file
# signals = np.random.rand(5, 256*300)*200 # 5 minutes of random signal
# channel_names = ['ch1', 'ch2', 'ch3', 'ch4', 'ch5']
# signal_headers = highlevel.make_signal_headers(channel_names, sample_rate=256)
# header = highlevel.make_header(patientname='patient_x', gender='Female')
# highlevel.write_edf('edf_file.edf', signals, signal_headers, header)

# read an edf file
signals, signal_headers, header = highlevel.read_edf('Data{}S001R01.edf'.format(os.sep))

front_data = []
front_meta = []
for i in range(64):
    d = signal_headers[i]
    # following are the signals we need...
    if 'Fpz.' in d.values():
        front_data.append(signals[i])
        front_meta.append('Fpz.')
    if 'Fp2.' in d.values():
        front_data.append(signals[i])
        front_meta.append('Fp2.')
    if 'Fp1.' in d.values():
        front_data.append(signals[i])
        front_meta.append('Fp1.')

# print(front_data)
# print(front_meta)
#to write csv :
with open("Data/frontal_data.csv",'w') as f:
    f.write(','.join(front_meta))
    f.write('\n')
    trans = np.array(front_data).T
    for line in trans:
        f.write(','.join(map(str, line)))
        f.write('\n')
