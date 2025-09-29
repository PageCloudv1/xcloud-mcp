# Development stage
FROM python:3.11-slim AS development

WORKDIR /app

# Install development and application dependencies
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

# Copy the rest of the application
COPY . .

# Expose port for the application and the debugger
EXPOSE 8000
EXPOSE 5678

# Command to run the application with the debugger
CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "server.py"]

# Test stage
FROM development AS test

# Run tests when the container launches
CMD ["pytest"]

# Production stage
FROM python:3.11-slim AS production

WORKDIR /app

# Install only production dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose port for the application
EXPOSE 8000

# Command to run the application
CMD ["python", "server.py"]
