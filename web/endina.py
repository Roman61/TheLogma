from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/")
def root():
    data = {"message": "Hello METANIT.COM"}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="192.168.5.70", port=80)
