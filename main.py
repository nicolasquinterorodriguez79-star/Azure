from fastapi import FastAPI

#instancia de FastAPI
app = FastAPI()

#EndPoint
@app.get("/")
def home():
    return{"mensaje":"Mi API esta funcionando"}




     
