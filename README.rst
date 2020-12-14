Gradebook plugin for `Tutor <https://docs.tutor.overhang.io>`__
================================================================

This Tutor plugin adds the `Gradebook <https://github.com/edx/frontend-app-gradebook/>`__ microfrontend to an Open edX installation.

⚠️ THIS IS ALPHA SOFTWARE NOT YET READY FOR RELEASE ⚠️

This plugin has the following limitations:

- Works with `Tutor <https://docs.tutor.overhang.io/>`__ >= 11.0.0
- Not compatible with Kubernetes deployment
- This plugin is not supported yet and will probably be extensively modified before it is included in the official list of supported Tutor plugins.

.. image:: https://github.com/overhangio/tutor-gradebook/raw/master/docs/screenshots/gradebook.png
  :alt: Gradebook screenshot
  :width: 500px
  :align: center

Installation
------------

::

    pip install tutor-gradebook

Usage
-----

Enable the `base <https://github.com/overhangio/tutor-mfe>`__ microfrontend and the gradebook plugins::

    tutor plugins enable mfe gradebook

Initialize the Gradebook service::

    tutor local quickstart
    # or, faster if you've already run quickstart:
    tutor local init --limit=gradebook

Then, follow the Open edX documentation on enabling the Gradebook: https://github.com/edx/frontend-app-gradebook/#configuring-for-local-use-in-edx-platform The settings do not need to be modified, but you will need to enable several waffle flags and switches.

The gradebook will then be available for every course at the following urls:

* In development: http://apps.local.overhang.io:1994/gradebook/<course-id>
* In production: http(s)://{{ MFE_HOST }}/gradebook/<course-id>

Configuration
-------------

- ``GRADEBOOK_DOCKER_IMAGE`` (default: ``"{{ DOCKER_REGISTRY }}overhangio/openedx-gradebook:{{ GRADEBOOK_VERSION }}"``)

License
-------

This software is licensed under the terms of the AGPLv3.
