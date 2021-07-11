FROM python:3.8-alpine

WORKDIR /app
COPY mymodule /app/mymodule
COPY tests /app/tests

CMD ["python", "-m", "mymodule.main"]