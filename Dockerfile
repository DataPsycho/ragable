FROM python:3.11-slim

RUN useradd -m -u 1000 user

USER user

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

COPY ./pyproject.toml ~/app/pyproject.toml
COPY src/ragable src/ragable
RUN pip install -e .

COPY src/frontend frontend
COPY chainlit.md .
EXPOSE 7860

CMD ["chainlit", "run", "frontend/app.py", "--port", "7860"]