FROM {{ MFE_DOCKER_IMAGE }}

# Clone gradebook app
ARG FRONTEND_APP_REPOSITORY=https://github.com/edx/frontend-app-gradebook
ARG FRONTEND_APP_VERSION={{ OPENEDX_COMMON_VERSION }}
RUN git clone $FRONTEND_APP_REPOSITORY --branch $FRONTEND_APP_VERSION --depth 1 .

# Install npm requirements
ARG NPM_REGISTRY=https://registry.npmjs.org/
RUN npm install --verbose --registry=$NPM_REGISTRY

ENV PORT 1994
