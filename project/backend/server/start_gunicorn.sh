#!/bin/bash

# serve at port 0.0.0.0:8003 and log to console
gunicorn server:app -b 0.0.0.0:8003 --access-logfile -