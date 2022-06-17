#!/usr/bin/env bash
. .vvenv/bin/activate
pip install -U -r requirements.txt
jupyter-notebook --ip='127.0.0.1'
deactivate
