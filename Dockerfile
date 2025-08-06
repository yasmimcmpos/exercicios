FROM python:3.14.0a7-alpine3.21
LABEL author="fazenda"
LABEL project="weekly-exercises-py"

# https://stackoverflow.com/a/49955098/7092954
RUN [ "addgroup", "-S", "appgroup" ]
RUN [ "adduser", "-S", "appuser", "-G", "appgroup" ]

USER root

RUN [ "apk", "update" ]
RUN [ "apk", "upgrade" ]
RUN [ "apk", "add", "--no-cache", \
  "gcc=14.2.0-r4", \
  "linux-headers=6.6-r1", \
  "mariadb-connector-c-dev=3.3.10-r0", \
  "musl-dev=1.2.5-r9", \
  "mysql-client=11.4.5-r0", \
  "pkgconf=2.3.0-r0", \
  "python3-dev=3.12.10-r0", \
  "rust=1.83.0-r0", \
  "sqlite-libs=3.48.0-r2" \
  ]
RUN [ "apk", "add", \
  "--repository=https://dl-cdn.alpinelinux.org/alpine/edge/community", \
  "poetry=2.0.1-r0" \
  ]

WORKDIR /usr/src/

USER appuser

COPY poetry.lock .
COPY pyproject.toml .

RUN [ "poetry", "install", "--no-root", "--no-interaction", "--no-ansi" ]

COPY tests/ tests/
COPY src/ src/