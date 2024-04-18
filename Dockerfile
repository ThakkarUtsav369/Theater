FROM python:3.10-slim as base

RUN apt-get update \
  && apt-get install -y --no-install-recommends python3-dev libpq-dev gcc \
  && rm -rf /var/lib/apt/lists/*
  # You can add additional steps to the build by appending commands down here using the
  # format `&& <command>`. Remember to add a `\` at the end of LOC 12.
  # WARNING: Changes to this file may cause unexpected behaviors when building the app.
  # Change it at your own risk.

WORKDIR /opt/webapp
COPY Pipfile* /opt/webapp/

RUN pip3 install --no-cache-dir -q 'pipenv==2023.7.23'
RUN pipenv install --deploy --system
COPY . /opt/webapp

FROM base as release

COPY --from=base /root/.local /root/.local
COPY --from=base /opt/webapp/manage.py /opt/webapp/manage.py


WORKDIR /opt/webapp
ENV PATH=/root/.local/bin:$PATH
ARG SECRET_KEY
RUN python3 manage.py collectstatic --no-input
