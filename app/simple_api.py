import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI application
# In a real scenario, this title might be fetched from config
app = FastAPI(title="ArgoCD Image Updater Demo", version="1.0.0")

class VersionInfo(BaseModel):
    application: str
    version: str
    environment: str
    pod_name: str
    message: str

@app.get("/", response_model=VersionInfo)
def get_version():
    """
    Root endpoint that returns version information.
    This is used to demonstrate the image update process.
    """
    version = os.getenv("APP_VERSION", "v1.0.0")
    pod_name = os.getenv("HOSTNAME", "local-dev")
    env = os.getenv("ENV", "development")
    
    return VersionInfo(
        application="version-demo",
        version=version,
        environment=env,
        pod_name=pod_name,
        message=f"Running version {version} in {env}"
    )

@app.get("/health")
def health_check():
    """
    Simple health check endpoint for Kubernetes liveness/readiness probes.
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    # Allow running directly for local development
    uvicorn.run(app, host="0.0.0.0", port=8000)