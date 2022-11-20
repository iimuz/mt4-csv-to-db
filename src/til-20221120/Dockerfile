FROM python:3.10.8-buster AS base

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV DEBIAN_FRONTEND=noninteractive

RUN set -x \
	&& : "Create the user" \
	&& groupadd --gid $USER_GID $USERNAME \
	&& useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

ENV DEBIAN_FRONTEND=dialog

USER $USERNAME
CMD ["python"]

FROM base AS development

USER root

RUN set -x \
  && : "Install packages for sqlite3." \
  && apt-get update -qq \
  && apt-get install -qq -y --no-install-recommends sqlite3 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER $USERNAME
