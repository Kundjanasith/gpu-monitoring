import os
import time
import datetime

command = "nvidia-smi --query-gpu=timestamp,name,pci.bus_id,driver_version,pstate,pcie.link.gen.max,pcie.link.gen.current,temperature.gpu,utilization.gpu,utilization.memory,memory.total,memory.free,memory.used --format=csv -l 1 >> data.csv"
#command = "nvidia-smi -f data.csv --format=csv"

while True:
    print(datetime.datetime.now())
    os.system(command)
    time.sleep(5)
