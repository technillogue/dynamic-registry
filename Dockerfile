FROM python:3.10 as deps
RUN python3.10 -m venv /app/venv 
RUN pip install poetry
WORKDIR /app/
COPY ./pyproject.toml /app/pyproject.toml
RUN VIRTUAL_ENV=/app/venv poetry install 

FROM python:3.10
WORKDIR /app/
COPY --from=deps /app/venv/lib/python3.10/site-packages /app/
COPY ./nginx_data.py ./whalesay_data.py ./registry.py /app/
COPY ./images /app/images/
ENTRYPOINT ["/usr/local/bin/python", "/app/registry.py"]
