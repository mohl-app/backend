from __future__ import annotations

import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health():
    return {"ok": True}


def main() -> None:
    reload = os.getenv("DEV", "0") == "1"
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8000")),
        reload=reload,
    )


if __name__ == "__main__":
    main()
