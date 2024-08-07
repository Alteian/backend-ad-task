#!/bin/bash

echo "Starting local server..."
exec $(which granian) --interface rsgi --host 0.0.0.0 --port 8000 --workers 1 --opt --reload --log-level debug src.main:app
