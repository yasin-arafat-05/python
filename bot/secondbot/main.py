from fastapi import FastAPI, Request
import uvicorn
app = FastAPI()

@app.post('/')
def read_root(req: Request):
    print(req.json())
    return {"hello": "world"}

if __name__ == '__main__':
    uvicorn.run("main:app",port=8000,host="0.0.0.0",reload=True)