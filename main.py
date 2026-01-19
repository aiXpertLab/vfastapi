from fastapi import FastAPI


app = FastAPI(
    title="VVV + FastAPI",
    description="VVV + FastAPI",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {
        "data": [
            {"id": 1, "name1": "Sample Item 1", "value": 100},
            {"id": 3, "name3": "Sample Item 3", "value": 300}
        ],
        "total": 2,
        "timestamp": "2024-01-01T00:00:00Z"
    }
