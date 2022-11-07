from fastapi import FastAPI
from analytics_producer import AnalyticsProducer

app = FastAPI()

# Method exposed to external services to provide the analytics
# of the last six months
@app.get("/get_analytics")
def get_analytics():
  json_data = AnalyticsProducer.get_analytics().to_json()
  return {"analytics": json_data}

