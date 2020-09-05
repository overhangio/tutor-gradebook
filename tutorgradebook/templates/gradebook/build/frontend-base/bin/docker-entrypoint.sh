#!/bin/sh -e
# TODO have a mechanism where multiple env files can be sourced one after the other, in alphabetical order

set -a # Cause all environment variables to be automatically exported
. /openedx/env
set +a

exec "$@"