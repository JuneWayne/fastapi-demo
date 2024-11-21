#!/bin/bash

cd app
uvicorn app.main:app --reload --port 8001

