from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"Welcome": "you"}

@app.get("/scrap")
async def root():
    return {"asdf": "sadf"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8080,
        host="0.0.0.0",
        # debug=True,
        # reload=True,
    )
#a<sdf