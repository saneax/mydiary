FROM python:3.11-slim

# Install system dependencies if any are needed (e.g., git, libsqlite3-dev)
RUN apt-get update && apt-get install -y --no-install-recommends 
    git 
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install tox
RUN pip install --no-cache-dir --upgrade pip tox ruff

# Set the working directory
WORKDIR /app

# The app code will be mounted by Jenkins
CMD ["tox"]
