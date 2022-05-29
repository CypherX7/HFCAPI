from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/bsc")
def bsc():
    f = open("./DATA.json",'r')
    data = f.read()
    f.close()
    return json.loads(data)["BSC"];

@app.get("/eth")
def ethx():
    f = open("./DATA.json",'r')
    data = f.read()
    f.close()
    return json.loads(data)["ETH"];

@app.get("/polygon")
def polygon():
    return {"DATA":"POLYGON"}
