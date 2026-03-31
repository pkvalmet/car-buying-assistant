import os
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

app = FastAPI(
    title="AI Car Buying Assistant",
    description=(
        "An intelligent AI-powered car buying assistant that helps users find the perfect vehicle. "
        "Features: multi-turn conversation, personalized recommendations, buy vs finance vs lease advisor, "
        "EV guidance with incentives, side-by-side comparison, and lease vs buy calculator. "
        "All prices and specs are approximate. Always verify with dealers before purchasing."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1", tags=["Car Buying Assistant"])


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to the AI Car Buying Assistant API",
        "docs": "/docs",
        "version": "1.0.0",
        "endpoints": {
            "chat": "POST /api/v1/chat",
            "compare": "POST /api/v1/compare",
            "lease_vs_buy_calculator": "POST /api/v1/calculate/lease-vs-buy",
            "session": "GET /api/v1/session/{session_id}",
            "health": "GET /api/v1/health",
        },
    }