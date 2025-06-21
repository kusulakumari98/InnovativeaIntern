import time
from google.cloud import monitoring_v3

def monitor_cpu_utilization(project_id):
    client = monitoring_v3.MetricServiceClient()
    project_name = f"projects/{project_id}"

    now = time.time()
    interval = monitoring_v3.TimeInterval(
        start_time={"seconds": int(now - 3600)},
        end_time={"seconds": int(now)}
    )

    results = client.list_time_series(
        request={
            "name": project_name,
            "filter": 'metric.type="compute.googleapis.com/instance/cpu/utilization"',
            "interval": interval,
            "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
        }
    )

    for result in results:
        print(result)
