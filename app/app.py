
from starlette.applications import Starlette
from routes import routes

app = Starlette(
    debug=True,
    routes=routes,
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")