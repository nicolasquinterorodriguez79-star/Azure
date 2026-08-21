from fastapi import FastAPI

#instancia de FastAPI
app = FastAPI()

#EndPoint
@app.get("/")
def home():
    return{"mensaje":"Mi API esta funcionando"}




num = (input("ingrese el numero"))
cifra = (input("ingrese la cifra"))
cont = 0
for i in num:
    if (i==cifra):
        cont=cont+1
print("la cifra", cifra, "aparece", cont, "de veces")        
