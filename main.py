import datetime
import uuid
import requests
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.validate import validate_data
from scripts.save_parquet import save_to_parquet

LINEAGE_ENDPOINT = "http://127.0.0.1:5001/lineage"

def send_lineage_event(step_name, inputs, outputs):
    event = {
        "eventType": "COMPLETE",
        "eventTime": datetime.datetime.utcnow().isoformat() + "Z",
        "run": {"runId": str(uuid.uuid4())},
        "job": {"name": f"health_etl_{step_name}", "namespace": "local.health_etl"},
        "inputs": [{"namespace": "local", "name": inp} for inp in inputs],
        "outputs": [{"namespace": "local", "name": out} for out in outputs]
    }
    try:
        requests.post(LINEAGE_ENDPOINT, json=event)
        print(f" Sent lineage event for {step_name}")
    except Exception as e:
        print(f" Failed to send lineage event: {e}")

def run_etl():
    raw_path = extract_data()
    send_lineage_event("extract", inputs=[], outputs=[raw_path])

    transformed_path = transform_data(raw_path)
    send_lineage_event("transform", inputs=[raw_path], outputs=[transformed_path])

    validate_data(transformed_path)
    send_lineage_event("validate", inputs=[transformed_path], outputs=[transformed_path])

    parquet_path = save_to_parquet(transformed_path)
    send_lineage_event("save_parquet", inputs=[transformed_path], outputs=[parquet_path])

    print(" ETL pipeline run completed.")

if __name__ == "__main__":
    run_etl()
