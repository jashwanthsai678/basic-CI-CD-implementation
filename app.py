from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Create limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# Add middleware
app.add_middleware(SlowAPIMiddleware)

# Custom error handler
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"error": "Rate limit exceeded. Try again later."}
    )

@app.get("/")
@limiter.limit("5/minute")   # 🔥 limit
def home(request: Request):
    return {"message": "API is running 🚀"}

@app.get("/predict/{number}")
@limiter.limit("10/minute")  # 🔥 limit
def predict(request: Request, number: int):
    result = "even" if number % 2 == 0 else "odd"
    return {"number": number, "prediction": result}