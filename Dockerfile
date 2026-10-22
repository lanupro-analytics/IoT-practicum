FROM mcr.microsoft.com/devcontainers/python:3.12

# Install Node.js LTS for Dragino JS payload decoder testing (Notebook 01)
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt-get update && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    python -m ipykernel install --user --name python3 --display-name "Python 3 (ipykernel)"

COPY . .

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--AllowRoot", "--ServerApp.token=''"]
