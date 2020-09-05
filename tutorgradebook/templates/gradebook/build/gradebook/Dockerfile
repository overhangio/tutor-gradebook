FROM {{ GRADEBOOK_FRONTEND_BASE_DOCKER_IMAGE }}

ARG FRONTEND_APP_REPOSITORY=https://github.com/edx/frontend-app-gradebook
ARG FRONTEND_APP_VERSION=open-release/juniper.3

RUN git clone $FRONTEND_APP_REPOSITORY --branch $FRONTEND_APP_VERSION --depth 1 .

# Install additional system requirements
RUN apk add --no-cache autoconf

ARG NPM_REGISTRY=https://registry.npmjs.org/
RUN npm install --verbose --registry=$NPM_REGISTRY

COPY Caddyfile /etc/caddy/Caddyfile

ENV PORT 1994