#!/bin/bash

# dont create and activate virtual environment if you already have one
if [ ! -d "venv" ]; then
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
fi


python3 main.py