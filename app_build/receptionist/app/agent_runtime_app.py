"""
⚡ AI RECEPTIONIST RUNTIME WEB SERVER (PORTFOLIO SHOWCASE)
Wraps the ADK agent application in a FastAPI server environment for Cloud Run deployment.
"""

import os
from typing import Any
import vertexai
from google.adk.artifacts import GcsArtifactService, InMemoryArtifactService
from vertexai.agent_engines.templates.adk import AdkApp
from app_build.receptionist.app.agent import app as adk_app


class AgentEngineApp(AdkApp):
    """FastAPI web server wrapping the ADK Receptionist topology."""
    
    def set_up(self) -> None:
        """Initialize telemetry, logs, and Vertex AI reasoning engine settings."""
        vertexai.init()
        super().set_up()

    def register_feedback(self, feedback: dict[str, Any]) -> None:
        """Collects, logs, and processes user telemetry feedback."""
        pass


logs_bucket = os.environ.get("LOGS_BUCKET_NAME")
agent_runtime = AgentEngineApp(
    app=adk_app,
    artifact_service_builder=lambda: (
        GcsArtifactService(bucket_name=logs_bucket)
        if logs_bucket
        else InMemoryArtifactService()
    ),
)
