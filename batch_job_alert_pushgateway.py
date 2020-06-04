import time
import random
from prometheus_client import Gauge, CollectorRegistry, pushadd_to_gateway

registry = CollectorRegistry()
duration = Gauge(
    'mybatchjob_duration_seconds',
    'Duration of batch job',
    registry=registry
)

try:
    with duration.time():
        print("调度任务就愉快的开始了！")
        time.sleep(random.randint(1, 10))
        #time.sleep(100)
        print("这里跑了我们的调度任务")
except:
    pass
else:
    last_success = Gauge(
        'mybatchjob_last_success',
        'Unixtime my batch job last succeeded',
        registry=registry
    )
    last_success.set_to_current_time()
finally:
    pushadd_to_gateway('10.8.8.61:9091', job='my_batch_job', registry=registry)
