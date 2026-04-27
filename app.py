from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

@app.get("/predict/{number}")
def predict(number: int):
    result = "even" if number % 2 == 0 else "odd"
    return {"number": number, "prediction": result}