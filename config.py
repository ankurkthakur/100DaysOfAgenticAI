"""
Shared configuration for all 100 Days scripts.
"""

import os
from openai import OpenAI

# Load API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is required.")

# Default models
TEXT_MODEL = "gpt-4o-mini"
IMAGE_MODEL = "gpt-image-1"

# Reusable OpenAI client
client = OpenAI(api_key=api_key)

def ensure_output_dir(folder: str = "output") -> str:
    """Create an output folder if needed and return its path."""
    import pathlib
    pathlib.Path(folder).mkdir(exist_ok=True)
    return folder
