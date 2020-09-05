##### Caddy image
FROM docker.io/alpine as caddy

RUN apk add --no-cache \
    curl

# Download the caddy static asset server
RUN curl -L "https://github.com/caddyserver/caddy/releases/download/v2.1.1/caddy_2.1.1_linux_amd64.tar.gz" --output /tmp/caddy.tar.gz \
    && mkdir /tmp/caddy \
    && tar xzf /tmp/caddy.tar.gz -C /tmp/caddy \
    && mv /tmp/caddy/caddy /usr/bin/ \
    && rm -rf /tmp/caddy.tar.gz /tmp/caddy

RUN mkdir /etc/caddy
COPY Caddyfile /etc/caddy/Caddyfile

##### Production image
FROM docker.io/node:12-alpine

RUN apk add --no-cache \
    curl git \
    # npm package system dependencies
    automake autoconf build-base libpng-dev pngquant
RUN mkdir -p /openedx/app
WORKDIR /openedx/app

COPY ./bin /openedx/bin
RUN chmod a+x /openedx/bin/*
ENV PATH /openedx/bin:./node_modules/.bin:${PATH}

# Create environment file
RUN touch /openedx/env
# Source environment file at runtime
ENTRYPOINT ["docker-entrypoint.sh"]

COPY --from=caddy /usr/bin/caddy /usr/bin/caddy
COPY --from=caddy /etc/caddy /etc/caddy

ENV PORT 8060
CMD caddy run --config /etc/caddy/Caddyfile