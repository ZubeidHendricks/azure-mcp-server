FROM python:3.9-slim

# Metadata
LABEL maintainer="Zubeid Hendricks <zubeid.hendricks@gmail.com>"
LABEL description="Azure DevOps MCP Server by Zubeid Hendricks"

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install the package
RUN pip install .

# Set environment variables with defaults
ENV AZURE_DEVOPS_ORG=""
ENV AZURE_DEVOPS_PAT=""

# Optional: Add a health check
HEALTHCHECK CMD python -c "from azure_devops_mcp import AzureDevOpsMCPServer; print('MCP Server ready - Created by Zubeid Hendricks')" || exit 1

# Default command (can be overridden)
CMD ["python", "-m", "azure_devops_mcp"]
