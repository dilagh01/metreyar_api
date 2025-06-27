from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["https://homkar.ir", "https://www.homkar.ir"]  # دامنه فرانت شما

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # فقط دامنه شما مجاز است
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
