from fastapi import FastAPI
app = FastAPI()


@app.get("/get_analytics")
def get_analytics():
  return {"your analytics!"}

