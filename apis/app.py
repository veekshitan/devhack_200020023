from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
import sys
import os
from endpoints import user_endpoints, buy_sell_endpoint, coupons_endpoints, events_endpoints
from core.settings import PORT, HOST
sys.path.append(os.path.realpath('.'))
app = FastAPI(title="BOT_BACKEND",
              description="Backend",
              version="0.1.0",
              redoc_url='/redoc')

origins = [
    "*"
]

app.include_router(user_endpoints.router)
app.include_router(buy_sell_endpoint.router)
app.include_router(coupons_endpoints.router)
app.include_router(events_endpoints.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run("app:app", host=HOST, port=PORT, reload=True)