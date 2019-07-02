#!/bin/bash

/usr/local/bin/python3.7 /opt/autoapi/geneve.py /opt/autoapi/generate.json

mv /opt/autoapi/generate.settings.py /opt/autoapi/settings.py

/usr/local/bin/python3.7 /opt/autoapi/app.py
