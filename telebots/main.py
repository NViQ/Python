from pyspectator.processor import Cpu
from time import sleep
cpu = Cpu(monitoring_latency=1)
with cpu:
    for _ in range(8):
       cpu.load, cpu.temperature
       sleep(1.1)