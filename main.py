from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

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
    f = open("./DATA.json",'r')
    data = f.read()
    f.close()
    return json.loads(data)["MATIC"];
