#!/usr/bin/env bash
. .venv/bin/activate
pip install -U -r requirements.txt
jupyter-notebook --ip='127.0.0.1'
deactivate
