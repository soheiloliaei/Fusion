# Fusion v15 - AI Agentic Operating System
# Multi-stage build for optimal production deployment

# Build stage
FROM python:3.10-slim as builder

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY pyproject.toml requirements.txt* ./

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -e .

# Production stage
FROM python:3.10-slim

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV FUSION_API_HOST=0.0.0.0
ENV FUSION_API_PORT=8000
ENV FUSION_MEMORY_DIR=/app/fusion_memory
ENV FUSION_TELEMETRY_DIR=/app/fusion_telemetry

# Create app user for security
RUN groupadd -r fusion && useradd -r -g fusion fusion

# Set working directory
WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p /app/fusion_memory /app/fusion_telemetry /app/logs && \
    chown -R fusion:fusion /app

# Switch to non-root user
USER fusion

# Expose API port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/status || exit 1

# Default command
CMD ["uvicorn", "fusion_api:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

# Alternative commands for different use cases
# CMD ["streamlit", "run", "web_app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
# CMD ["python", "fusion.py", "pipeline", "Your prompt here"] 