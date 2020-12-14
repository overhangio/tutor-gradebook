from glob import glob
import os

from .__about__ import __version__

HERE = os.path.abspath(os.path.dirname(__file__))

templates = os.path.join(HERE, "templates")

config = {
    "add": {"OAUTH2_SECRET": "{{ 24 | random_string }}"},
    "defaults": {
        "VERSION": __version__,
        "FRONTEND_BASE_DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}overhangio/openedx-frontend-base:{{ GRADEBOOK_VERSION }}",
        "DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}overhangio/openedx-gradebook:{{ GRADEBOOK_VERSION }}",
        "PUBLIC_PATH": "/gradebook",
    },
}

hooks = {
    "build-image": {
        "gradebook": "{{ GRADEBOOK_DOCKER_IMAGE }}",
    },
    "remote-image": {
        "gradebook": "{{ GRADEBOOK_DOCKER_IMAGE }}",
    },
    "init": ["gradebook", "lms"],
}


def patches():
    all_patches = {}
    for path in glob(os.path.join(HERE, "patches", "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
