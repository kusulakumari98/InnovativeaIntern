from google.cloud import logging

def log_event(project_id, message):
    client = logging.Client(project=project_id)
    logger = client.logger("multi_tenant_log")
    logger.log_text(message)
    print("Logged:", message)
