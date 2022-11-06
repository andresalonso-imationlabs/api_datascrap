from fastapi import FastAPI, Request
import uvicorn
from lxml import html
import requests
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"Welcome": "you"}

@app.get("/scrap/{url}/{key_element}/{key_find_by}/{key_id}")
def read_root(url: str, key_element: str, key_find_by: str, key_id: str, request: Request):
     page = requests.get("http://WWW."+url)
     tree = html.fromstring(page.content)
     #return tree

     rows = tree.xpath("//"+key_element+"[contains(@"+key_find_by+", '"+key_id+"')]//text()")
     return rows

'''
async def scrapXpathkey(url, key):
        page = requests.get(url)
        tree = html.fromstring(page.content)        
        rows = tree.xpath(key)
        return rows
'''


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8080,
        host="0.0.0.0",
        # debug=True,
        # reload=True,
    )
#a<sdf