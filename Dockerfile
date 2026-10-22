FROM python:3.12-slim

# Install git, curl, and Node.js LTS for Dragino JS payload decoder testing (Notebook 01)
RUN apt-get update && \
    apt-get install -y --no-install-recommends git curl build-essential && \
    curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    python -m ipykernel install --user --name python3 --display-name "Python 3 (ipykernel)"

COPY . .

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--AllowRoot", "--ServerApp.token=''"]
